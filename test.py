import sys
import datatime

time = datatime.datetime.now()

output = "Hi %s current time is %s" % (sys.argv[1], time)

print(output)