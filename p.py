#!/usr/bin/env python

import os
import sys
import logging


# can define funcs for module "p"
def setLog(l):
	logging.basicConfig(level=l)



# Main
def main():
	# whatever
	logging.debug("main")


if __name__ == '__main__':
	# just supports stdin, and set of option letters 
	pname = sys.argv[0]

	if (len(sys.argv)>1):
			for c in sys.argv[1]:
				if (c == 'd'):
					debug=1
					setLog(logging.DEBUG)
				elif (c=='n'):
					noop=1
				elif (c=='-'):
					pass # ignore
				else:
					logging.warn("bad option: %c", c)

	# or if (len(sys.argv)==3):
	#		fname=sys.argv[2]

	logging.debug("starting: %s", pname)
	main()
	sys.exit(0)
