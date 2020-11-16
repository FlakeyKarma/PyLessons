#!/bin/python3

#Just some filler text to be logged
import time

#The file object to create and write to file
LOG_FIL = open("time.log", 'a')

#Write update to file!
LOG_FIL.write(str("logEx.py ran at %s!\n" % (time.asctime())))
