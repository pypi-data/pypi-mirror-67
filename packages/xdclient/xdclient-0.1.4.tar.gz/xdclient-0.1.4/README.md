XDClient is a command line git log collector client for agilean/lean team effectiveness analysis tool [X-Developer](https://x-developer.cn).

Currently it supports both python 2.7.x and 3.5+.

## Why Should I Use This?

The reason to use xdclient is that it provides ability to intergrate team effectiveness analysis with CI(Continuous Intergration Server) via command line.

It allows you to pre-install the package and add an `exec command` in your pipeline file.

## Features

- Config APPID/KEY and TeamID via parameters
- Generates git log
- Specify master/dev(default) branches
- Communicates with X-Developer analysis server and response status
- Send git log to X-Developer and start analysis

## Installation

```
pip install xdclient
```

## Usage

Specify the `appid` `appkey` `teamid` from your X-Developer account.

```
python -m xdclient -i {appid} -k {appkey} -t {teamid}
```

### Options

```
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i APPID, --appid=APPID
                        The information of appid in your home page
  -k APPKEY, --appkey=APPKEY
                        The information of appkey in your home page
  -t TEAM, --team=TEAM  The team id you created
  -p PATTERN, --pattern=PATTERN
                        Sensitive words
  -f FORCE, --force=FORCE
                        Force Analysis
  -m MASTER, --master=MASTER
                        Master
```

### Resources

- [X-Developer](https://x-developer.cn)