#
# This makefile is used by the "stack create package" command to turn any
# directory into an RPM copied into the contrib area.
#
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

PKGROOT         = /opt/stack
REDHAT.ROOT     = $(CURDIR)
include $(STACKBUILD)/etc/CCRules.mk

build:

install::
	mkdir -p $(ROOT)/$(PREFIX)
	cp -a $(SOURCE_DIRECTORY) $(ROOT)/$(PREFIX)/

dir2pkg:
	$(MAKE) pkg
	mv $(REDHAT.ROOT)/RPMS/$(ARCH)/* $(DEST_DIRECTORY)
