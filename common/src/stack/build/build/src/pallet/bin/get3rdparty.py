#!/usr/bin/python
#
# @copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v5.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

import os
import sys
import subprocess

urlbase   = 'https://teradata-stacki.s3.amazonaws.com/3rdparty'
manifest  = 'manifest.3rdparty'
cachedir  = '3rdparty'
docfile   = '3rdparty.md'
resources = { }

if not os.path.exists(manifest):
	print('Cannot file manifest.3rdparty file')
	sys.exit(0)

if not os.path.exists(cachedir):
	os.mkdir(cachedir)

fin = open(manifest, 'r')
for line in fin.readlines():
	resource = line.strip()
	resources[resource] = os.path.join(urlbase, resource)
fin.close()

for resource in resources:
	target = os.path.join(cachedir, resource)
	if not os.path.exists(target):
		print('download %s\n\t%s' % (resource, resources[resource]))
		subprocess.call([ 'curl',
				  '-sSo%s' % target,
				  resources[resource] ])

fout = open(docfile, 'w')
fout.write("""# Third Party Resources

This repository includes the following code from other projects.

""")
for resource in resources:
	fout.write('* %s [%s]\n' % (resource, resources[resource]))

fout.close()









