
import os
import sys
import logging

# just supports stdin, and set of option letters 
pname = sys.argv[0]

debug=0

if (len(sys.argv)>1):
		for c in sys.argv[1]:
			if (c == 'd'):
				debug=1
				logging.basicConfig(level=logging.DEBUG)
			elif (c=='n'):
				noop=1
			elif (c=='-'):
				pass # ignore
			else:
				logging.warn("bad option: %c", c)

# or if (len(sys.argv)==3):
#		fname=sys.argv[2]

logging.debug("starting: %s", pname)
