#!/usr/bin/python

import time
import sys
import string

updateCounts = {}

def follow(thefile):
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         yield line

logfile = open("/var/log/quagga/debug.log")
loglines = follow(logfile)
for line in loglines:
    strArray = string.split(line.rstrip(), ',')
    origin = strArray[-1].split()[-1]
    if "path" in line:
        if origin in update_counts:
           updateCounts[origin] += 1
        else:
           updateCounts[origin] = 1
        print 'Origin ' + origin +'\tCount ' + str(updateCounts[origin]) + '  \t| AS ' + strArray[-1]
        #sys.stdout.write(line)
