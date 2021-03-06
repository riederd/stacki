# @copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v5.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

import subprocess
import json

__stack__ = '/opt/stack/bin/stack'

rc = None


def ReturnCode():
	"""
	Get the return code of the previously run command.
	"""
	return rc


def Call(cmd, args=None, format='json', sudo=False):
	"""
	Call the Stack Command Line and return a python dictionary as the
	result.  Currently only works with list commands.

	Example:
		result = stack.api.Call('list network', [ 'private' ])
	"""

	global rc
	
	command = cmd.replace('.', ' ').strip().split()
	
	if sudo:
		list = [ sudo ]
	else:
		list = [ ]
	list.append(__stack__)
	list.extend(command)
	if args:
		list.extend(args)

	if command[0] == 'list':
		list.append('output-format=%s' % format)
	
	s = None
	p = subprocess.Popen(list, stdout=subprocess.PIPE)
	for line in p.stdout.readlines():
		if not s:
			s = line
		else:
			s += line
	rc = p.wait()
	if rc:
		return [ ]

	if command[0] == 'list':
		if s:
			return json.loads(s)
		return [ ]
	
	if s:
		return s.split('\n')
	return [ ]


