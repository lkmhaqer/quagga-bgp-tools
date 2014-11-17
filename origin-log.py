#!/usr/bin/python

import time
import sys
import string

update_counts = {}

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
    str_array = string.split(line.rstrip(), ',')
    origin = str_array[-1].split()[-1]
    if "path" in line:
        if origin in update_counts:
           update_counts[origin] += 1
        else:
           update_counts[origin] = 1
        print 'Origin ' + origin +'\tCount ' + str(update_counts[origin]) + '  \t| AS ' + str_array[-1]
        #sys.stdout.write(line)
