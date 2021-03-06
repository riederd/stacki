# @copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v5.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

import stack.commands


class Plugin(stack.commands.Plugin):
	"Writes /etc/hosts"

	def provides(self):
		return 'hostfile'

	def requires(self):
		return []

	def run(self, args):
		self.owner.command('sync.host')
