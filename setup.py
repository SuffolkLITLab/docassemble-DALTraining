import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.DALTraining',
      version='1.0.0',
      description=('New interview builder training templates'),
      long_description="# Document Assembly Line training resources\r\n\r\nThis repository contains resources for the [Suffolk LIT Lab](https://suffolklitlab.org/)'s Document Assembly Line trainings.\r\n\r\n## New interview builder trainings\r\n\r\n### Session 1: Hello, world!\r\n\r\nThis session is an introduction to “vanilla” Docassemble. At the end of this session, you will be able to create simple interviews that generate completed documents.\r\n\r\nBefore this session, attendees should:\r\n\r\n1.\tRegister an account on the [LIT Lab dev server](https://apps-dev.suffolklitlab.org/)\r\n2.\tEmail [litlab@suffolk.edu](mailto:litlab@suffolk.edu) to request developer privileges (include the email you used to register)\r\n\r\nOutline:\r\n\r\n1. Introduction to the Docassemble Playground\r\n2. Create your first question\r\n3. Working with common question types\r\n4. Specifying the order of questions\r\n5. Dynamic questions\r\n6. Basic document assembly\r\n7. Using Word and Acrobat templates\r\n\r\n## Session 2: The Weaver and other Assembly Line tools\r\n\r\nThis session is an introduction to the Document Assembly Line tools, especially the Weaver. At the end of this session you will be able to use the Weaver to generate a draft Docassemble interview from an existing court form.\r\n\r\n## Session 3: Troubleshooting\r\n\r\nIn this session we will go over common coding issues and how to solve them, plus general troubleshooting tips and a hands-on problem-solving session.",
      long_description_content_type='text/markdown',
      author='Sam Glover',
      author_email='sam.glover@suffolk.edu',
      license='The MIT License (MIT)',
      url='https://assemblyline.suffolklitlab.org/',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/DALTraining/', package='docassemble.DALTraining'),
     )

