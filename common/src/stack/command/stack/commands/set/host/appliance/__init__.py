# @copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v5.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

import stack.commands
from stack.exception import ArgRequired, CommandError


class Command(stack.commands.set.host.command,
	      stack.commands.ApplianceArgumentProcessor):
	"""
	Set the Appliance for a list of hosts.
	
	<arg type='string' name='host' repeat='1'>
	One or more host names.
	</arg>

	<param type='string' name='appliance' optional='0'>
	Appliance name (e.g. "backend").
	</param>
	"""

	def run(self, params, args):
		
		(appliance, ) = self.fillParams([ ('appliance', None, True) ])
		
		if not len(args):
			raise ArgRequired(self, 'host')

		if appliance not in self.getApplianceNames():
			raise CommandError(self, 'appliance parameter not valid')

		for host in self.getHostnames(args):
			self.db.execute("""
				update nodes set appliance=
				(select id from appliances where name = '%s')
				where name='%s'
				""" % (appliance, host))
			

