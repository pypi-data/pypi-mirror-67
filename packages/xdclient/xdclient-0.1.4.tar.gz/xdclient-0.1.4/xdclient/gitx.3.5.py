# encoding: utf-8
import optparse
import os
import re
from requests_toolbelt import MultipartEncoder
import requests
from datetime import datetime
import sys

ANALYSIS_URL = 'http://localhost:8000/analysis/update/'


class Cli(object):
    def __init__(self):
        parser = optparse.OptionParser(description='Git-x: A Git Log Collect Tool',
                                       prog='gitx',
                                       version='0.0.1',
                                       usage='%prog -i -k -t -l -p -f -m')
        parser.add_option('--appid', '-i', default="",
                          help='The information of appid in your home page')
        parser.add_option('--appkey', '-k', default="",
                          help='The information of appkey in your home page')
        parser.add_option('--team', '-t', default="",
                          help='The team id you created')
        parser.add_option('--pattern', '-p', default="",
                          help='Sensitive words')
        parser.add_option('--force', '-f', default="",
                          help='Force Analysis')
        parser.add_option('--master', '-m', default="",
                          help='Master')

        self.options, self.args = parser.parse_args()
        print('开始同步采集器...')
        appid = self.options.appid
        appkey = self.options.appkey
        team = self.options.team
        pattern = self.options.pattern or '国网|电力'
        force = self.options.force or False
        master = self.options.master or False

        # 获得当前目录名称
        path = os.path.realpath('.')
        log = os.path.basename(path)
        log = log.replace(' ', '')

        if log and appid and appkey and team:
            log_file = os.path.realpath(path + '/' + log + '.csv')
            if os.path.isfile(log_file):
                os.remove(log_file)
            cmd = 'git log --pretty=format:"%an,%ae,%ai,%s" >> {}.csv'.format(
                log)
            os.system(cmd)
            # 获取最后更新时间
            cmd = 'git log --pretty=format:"%at" -1'
            output = os.popen(cmd)
            lastCommitted = output.readline()
            res = requests.get(ANALYSIS_URL, params={
                'appid': appid,
                'appkey': appkey,
                'team': team,
                'log': log,
                'logPath': log_file,
                'lastCommitted': lastCommitted,
                'force': force,
                'master': master
            }).json()
            if res['status'] == 'success':
                print('采集器同步结果：成功。')
                data_sources = res['dataSources']
                params = {
                    'appid': appid,
                    'appkey': appkey,
                    'team': team,
                    'master': str(master),
                    'logCount': str(len(data_sources.keys()))
                }
                index = 0
                flag = False
                for log in data_sources:
                    log_path = data_sources.get(log)
                    if log_path:
                        if os.path.isfile(log_path):
                            flag = True
                            f = open(log_path, 'rb')
                            log_sen_path = log_path + '.bak'
                            new_file = open(log_sen_path, 'wb')
                            for line in f:
                                if (re.search(pattern, line.decode('utf-8'), flags=0)):
                                    line = re.sub(pattern, '***', line)
                                new_file.write(line)
                            f.close()
                            new_file.close()

                            params.update(
                                {'log' + str(index): (log, open(log_sen_path, 'rb'), 'application/csv')})
                            index += 1
                if flag:
                    m = MultipartEncoder(
                        fields=params)
                    print('分析开始...')
                    response = requests.post(ANALYSIS_URL, data=m, headers={
                        'Content-Type': m.content_type}).json()
                    if response['status'] == 'success':
                        print('分析结果：成功。')
                        print('已分析'+str(index)+'个仓库最新日志。')
                    else:
                        print('分析结果：失败。')
                        message = '失败原因：' + response['message']
                        print(message)
                        sys.exit(1)
                    for log in data_sources:
                        log_path = data_sources.get(log)
                        log_sen_path = log_path + '.bak'
                        if os.path.isfile(log_sen_path):
                            os.remove(log_sen_path)
                else:
                    print('已更新'+log+'日志最新提交时间。')
            else:
                print('采集器同步结果：失败。')
                print('错误原因：' + res['status'])
                sys.exit(1)
            sys.exit(0)
        else:
            parser.print_help()
