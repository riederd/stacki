# @copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v5.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@
#
# @rocks@
# Copyright (c) 2000 - 2010 The Regents of the University of California
# All rights reserved. Rocks(r) v5.4 www.rocksclusters.org
# https://github.com/Teradata/stacki/blob/master/LICENSE-ROCKS.txt
# @rocks@

import stack.commands


class command(stack.commands.HostArgumentProcessor,
	stack.commands.list.command):
	pass
	

class Command(command):
	"""List the Appliance, and physical position info for a list of
	hosts.

	<arg optional='1' type='string' name='host' repeat='1'>
	Zero, one or more host names. If no host names are supplied, info about
	all the known hosts is listed.
	</arg>

	<example cmd='list host backend-0-0'>
	List info for backend-0-0.
	</example>

	<example cmd='list host'>
	List info for all known hosts.
	</example>

	"""
	def run(self, params, args):
	    
		(order, ) = self.fillParams([ ('order', 'asc') ])
		
		hosts = self.getHostnames(args, order=order)
	    
		header = [ 'host' ]
		values = { }
		for host in hosts:
			values[host] = [ ]
			
		for (provides, result) in self.runPlugins(hosts):
			header.extend(result['keys'])
			for h, v in result['values'].items():
				values[h].extend(v)

		self.beginOutput()
		for host in hosts:
			self.addOutput(host, values[host])
		self.endOutput(header=header, trimOwner=False)

