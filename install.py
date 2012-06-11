#/usr/bin/env python2.6
# ----------------------------------------------------------------------------------
# 
# Copyright (C) 2011-2012 Piotr Styk
# 
# ----------------------------------------------------------------------------------
# 
# LICENSE:
# 
# This file is part of tv.styk.storage.oi.zfs.nfs.
# 
# tv.styk.storage.oi.zfs.nfs is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# tv.styk.storage.oi.zfs.nfs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with tv.styk.storage.oi.zfs.nfs; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 

import os
import subprocess

RUN_PATH = os.path.dirname(__file__)

# install setuptools
out = subprocess.Popen(['sudo', 'pkg', 'install', 'pkg:/library/python-2/setuptools-26'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
print out
# install virtualenv
out = subprocess.Popen(['sudo', 'easy_install', 'virtualenv'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
print out
# create bottle virtualenv
os.mkdir(os.path.join(RUN_PATH, 'env'))
out = subprocess.Popen(['virtualenv', 'env/zfs.status'], stdout=subprocess.PIPE).communicate()[0]
print out
# install bottle, paster
out = subprocess.Popen(['./env/zfs.status/bin/pip', 'install', 'bottle'], stdout=subprocess.PIPE).communicate()[0]
print out
out = subprocess.Popen(['./env/zfs.status/bin/pip', 'install', 'paste'], stdout=subprocess.PIPE).communicate()[0]
print out
# install git
out = subprocess.Popen(['sudo', 'pkg', 'install', 'pkg:/developer/versioning/git'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
print out
# download status app
os.mkdir(os.path.join(RUN_PATH, 'apps'))
out = subprocess.Popen(['git', 'clone', 'git://github.com/styk-tv/tv.styk.storage.oi.zfs.nfs.git', 'apps/status'], stdout=subprocess.PIPE).communicate()[0]
print out
print "To start zfs.status - source " + os.path.join(RUN_PATH, 'env') + '/zfs.status/bin/activate, cd apps/status, python status.py, browse http://127.0.0.1:8080/status'

