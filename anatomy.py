#!/usr/bin/python -- this is only for MAC or linux
# Example python script -- this is a standard comment
import sys
argc = len(sys.argv)
if argc > 1:
    print('Too many args')
else:
    where = 'World'
    print("Hello", where)
print('Goodbye from ' + sys.argv[0])