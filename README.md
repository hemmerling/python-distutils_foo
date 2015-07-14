Welcome to "distutils_foo"
==========================

"distutils_foo" is a Python demo application prepared for distribution by distutils
http://docs.python.org/2/distutils/

It shows how to write a Python application
and a Python setup script, which can be distributed and
installed on a different computer easily. It is also an
example for the renaming of packages for distribution.

So it's for education.
I learned by creating the project, that you should'nt put a Python module and a Python package with same name in a directory ( which you can easily do on Windows,.. ).

Requirements
------------

"distutils_foo" is for Python 2.7 and is prepared to run on Python 3.x ( untested ).

It was tested with Python 2.7 on Windows.


Step 1: Download+Unzipping
--------------------------

On Unix / Linux:
Download "distutils_foo"-master.zip from GitHub into your home directory
/home/<yourname>

Extract from that directory: unzip distutils-master.zip
The distutils directory will be created and populated under /home/<yourname>

On Windows:
Download "distutils_foo"-master.zip from GitHub and unzip it into any directory, e.g.
C:\users\public\distutils_foo


Step 2: : Installation from the development directory
-----------------------------------------------------

Open a console in the extraction path and execute:

```
python setup.py install
```

Using pip:

```
pip install distutils_foo
```


Alternative step 2: Installation of a distribution
--------------------------------------------------

Step 2a: Generation of a distribution
-------------------------------------

Open a console in the extraction path and execute:

```
python setup.py sdist
```

This creates, in case of version 1.00, the zip archive

"dist/distutils_foo-1.0.zip"


Open a console in the directory "dist" and unzip the just created archive:

```
unzip distutils_foo-1.0.zip
```

This creates, in case of version 1.00, the directory

"distutils_foo-1.0.zip"


Step 2b: Installation of the distribution
-----------------------------------------

Open a console in the directory "distutils_foo-1.0" ( in case of version 1.00 ) and execute:

```
python setup.py install
```

Using pip:

```
pip install distutils_foo
```


Usage
=====

You may  call "distutils_foo" on commandline by

```
distutils_foo-script
```

or by operatings-system specific commands
on Windows:

```
distutils_foo.bat
```

and on Linux:

```
distutils_foo.sh
```

from any directory of the filesystem of your operating system.
It displays a copyright message and messages which prove that it
may load some other project modules ( subfoo and subfoo2 ) and
creates the files "subfoo.txt" and "subfoo2.txt"
in the current directory from which it was called.


Documentation
=============

Visit the

"distutils_foo" GitHub.io page http://hemmerling.github.com/python-distutils_foo
and the "distutils_foo" Wiki http://www.github.com/hemmerling/python-distutils_foo/wiki
for more documentation.

History
=======

2015-07-01 - First public version 1.00
