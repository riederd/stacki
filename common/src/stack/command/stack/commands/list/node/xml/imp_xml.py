# @copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v5.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

from xml.sax import make_parser
import stack.commands


class Implementation(stack.commands.Implementation):

	def __init__(self, command):
		stack.commands.Implementation.__init__(self, command)
		self.parser = make_parser()

	def run(self, args):

		filename = args[0]
		handler  = args[1]

		fin = open(filename, 'r')
		self.parser.setContentHandler(handler)
		self.parser.parse(fin)
		fin.close()

		
