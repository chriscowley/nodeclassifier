from __future__ import print_function
from setuptools import setup, find_packages
#from setuptools.command.test import test as TestCommand
import os

def read(fname):
    """ function to read in a file """
    # intentionally *not* adding an encoding option to open
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='nodeclassifier',
    version='0.1.0',
    maintainer='Chris Cowley',
    maintainer_email='chris@chriscowley.me.uk',
    url='https://chriscowley.me.uk',
    description='Helps classifier nodes for Puppet',
    long_description=read('README.md'),
    packages=['nodeclassifier'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    zip_safe=False,
    install_requires=find_packages(exclude=["tests/"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
    ],
)
