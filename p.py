#!/usr/bin/env python

import os
import sys
import logging
import unittest


# can define funcs for module "p"
def setLog(l):
	logging.basicConfig(level=l)

def someFunc():
	logging.debug("someFunc")
	
class PClass(object):
	def __init__(self, x):
		self.x = x

	def __str__(self):
		return "PClass(" + str(self.x) + ")"

	def value(self):
		return self.x

# Test Code
class PUnitTest(unittest.TestCase):
	def setUp(self):
		# can do one time setup here
		self.p = PClass(2)

	def test_obj_is_ok(self):
		self.assertEqual( 2, self.p.value() )

# Main
def main():
	# whatever
	logging.debug("main")
	p = PClass(9)
	print p


if __name__ == '__main__':
	# just supports stdin, and set of option letters 
	pname = sys.argv[0]

	runFunc = main	
	if (len(sys.argv)>1):
			for c in sys.argv[1]:
				if (c == 'd'):
					debug=1
					setLog(logging.DEBUG)
				elif (c=='t'):
					runFunc = unittest.main
					sys.argv.remove(sys.argv[1]) # add unittest args after 
					break
				elif (c=='-'):
					pass # ignore
				else:
					logging.error("bad option: %c", c)
					print("usage: [-d]   - debug")
					print("usage: [-t  [unittest args]  - test")
					sys.exit(-1)

	# or if (len(sys.argv)==3):
	#		fname=sys.argv[2]

	logging.debug("starting: %s", pname)
	runFunc()
	sys.exit(0)
