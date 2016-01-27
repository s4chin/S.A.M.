#!/usr/bin/env python
import sys

from src.daemon import Daemon
from src.stt import gstt

class MyDaemon(Daemon):
    def run(self):
        gstt()


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/sam.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "Usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
