#!/usr/bin/env python

import os
import sys
import logging
import unittest
from optparse import OptionParser

#### Functions for this module/main
def setLog(l):
	logging.basicConfig(level=l)

def someFunc():
	logging.debug("someFunc")
	
#### A Class
class PClass(object):
	def __init__(self, x):
		self.x = x

	def __str__(self):
		return "PClass(" + str(self.x) + ")"

	def value(self):
		return self.x

#### Test Code
class PUnitTest(unittest.TestCase):
	def setUp(self):
		# can do one time setup here
		self.p = PClass(2)

	def test_obj_is_ok(self):
		logging.debug("test_obj_is_ok")
		self.assertEqual( 2, self.p.value() )

#### Main
def main():
	logging.debug("main")
	p = PClass(9)
	print p
	# to read stdin or all files on argv
	# import fileinput
	# for line in fileinput.input()
	#	print line


if __name__ == '__main__':
	# just supports stdin, and set of option letters 
	pname = sys.argv[0]

	op = OptionParser(usage="%prog [-d] [-t]", version="%prog 0.5")
	op.add_option("-d", "--debug", dest="debugFlag", action="store_true", default=False)
	op.add_option("-t", "--test", dest="doTest", action="store_true", default=False)
	(options, args) = op.parse_args()
	
	print "args: ", len(args)
	runFunc = main	
	if (options.debugFlag):
		setLog(logging.DEBUG)
	if (options.doTest):
		print('dotest')
		runFunc = unittest.main
		del sys.argv[1:]
		# other args will be parsed by unittest.main

	# or if (len(sys.argv)==3):
	#		fname=sys.argv[2]

	logging.debug("starting: %s", pname)
	runFunc()
	sys.exit(0)
