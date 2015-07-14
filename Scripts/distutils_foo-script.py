#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#
#  @package   distutils_foo
#  @file      distutils_foo-script.py
#  @brief     Python demo application prepared for distribution by distutils
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

from __future__ import print_function
import distutils_foo_module

##
#
#  @fn       main
#  @brief    Execute the software
#
def main():
    """main"""
    distutils_foo_module.main()
    return
##
#
#  @fn       __main__
#  @brief    Execute the software
#
if __name__ == '__main__':
    main()


print("distutils_foo-script")
XXX = open("zzzz4.txt", "w+")
XXX.write("zzzz4.txt")
XXX.close()
print(XXX)
