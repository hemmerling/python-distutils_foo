#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
#
#  @package   distutils_foo
#  @file      distutils_foo_module.py
#  @brief     Python demo application prepared for distribution by distutils
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @date      2014-11-06
#  @copyright Apache License, Version 2.0
#
#  distutils_foo - Python demo application prepared for distribution
#                  by distutils
#
#  Copyright 2014 Rolf Hemmerling
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""distutils_foo.py"""

from __future__ import print_function
import sys
try:
    from distutils_foo_package import module1
except:
    from dev_package1 import module1

##
#
#  @fn       write
#  @brief    Print message
#
def write(contents):
    """write"""
    print (contents)
    return

##
##
#
#  @fn       copyright_message
#  @brief    Display copyright notice
#
def copyright_message():
    """main"""
    message = \
    "distutils_foo - " + \
    "Python demo application prepared for distribution by distutils\n" + \
    "Copyright 2014 Rolf Hemmerling\n" + \
    "Licensed under the Apache License, Version 2.0 (the 'License');\n" + \
    "you may not use this file except in compliance with the License.\n" + \
    "You may obtain a copy of the License at\n" + \
    "http://www.apache.org/licenses/LICENSE-2.0\n" + \
    "Unless required by applicable law or agreed to in writing, software\n" + \
    "distributed under the License is distributed on an 'AS IS' BASIS,\n" + \
    "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, " + \
    "either express or implied.\n" + \
    "See the License for the specific language governing permissions and\n" + \
    "limitations under the License.\n"

    if len(sys.argv) == 1:
        write(message)
    return

##
#
#  @fn       main
#  @brief    Execute the software
#
def main():
    """main"""
    copyright_message()
    return

##
#
#  @fn       __main__
#  @brief    Execute the software
#
#if __name__ == '__main__':
#    main()

print("distutils_foo_module")
XXX = open("zzzz3.txt", "w+")
XXX.write("zzzz3.txt")
XXX.close()
print(XXX)


