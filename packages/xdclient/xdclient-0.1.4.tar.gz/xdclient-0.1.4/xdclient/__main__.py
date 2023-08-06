import sys
from xdclient.gitx import Cli

if __name__ == '__main__':
    try:
        cli = Cli()
    except Exception as e:
        print("ERROR: %s" % str(e))
        sys.exit(1)