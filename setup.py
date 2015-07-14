#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#
#  @package   distutils_foo
#  @file      setup_subfoo5.py
#  @brief     Setup for distribution of a demo application by distutils
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @date      2015-07-01
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  distutils_foo - Python demo application prepared for distribution
#                  by distutils
#
#  Copyright 2015 Rolf Hemmerling
#
#  Licensed under the GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""

from distutils.core import setup
# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

##
#
#  @function    setup
#  @brief       Setup for distutils_foo
setup(name='distutils_foo',
      version='1.0',
      description=\
      'distutils_foo - Demo application prepared for distribution by distutils',
      long_description=\
      'distutils_foo - Demo application prepared for distribution by distutils',
      author='Rolf Hemmerling',
      author_email='hemmerling@gmx.net',
      # maintainer='Rolf Hemmerling',
      # maintainer_email='hemmerling@gmx.net',
      url='http://www.github.com/hemmerling/distutils_foo/',
      download_url='http://www.github.com/hemmerling/distutils_foo',
      license='Apache License, Version 2.0',
      platforms=['Python 2.7 on Windows and Linux'],
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 1',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'License :: Apache License, Version 2.0',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: Linux :: Ubuntu',
                   'Topic :: Python :: Distutils',
                   'Topic :: Python :: Application :: Setup',
                   'Topic :: Python :: Application :: Setup :: Distutils',
                   'Topic :: Python :: Application :: Installation',
                   'Topic :: Python :: Application :: Distribution'],
      data_files=[('Lib/site-packages/distutils_foo_package',\
                   ['AUTHORS', 'COPYING', 'README.txt']),
                  ('Scripts',\
                   ['Scripts/distutils_foo.bat', 'Scripts/distutils_foo.sh'])
                 ],
      scripts=['Scripts/distutils_foo-script.py'],
      py_modules=['Scripts/distutils_foo-script', 'distutils_foo_module'],
      package_dir={'distutils_foo_package': 'dev_package1', \
                   'distutils_foo_package/dist_package2': \
                   'dev_package1/dev_package2'},
      packages=['distutils_foo_package', 'distutils_foo_package/dist_package2'],
      requires=['required_module'],
      provides=['provided_module'],
      obsoletes=['obsolete_module'],
      keywords=['distutils_foo', 'distutils','setup.py', 'deployment',
                'installation'])
