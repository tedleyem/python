import os 
import platform
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

if platform.system() == "Windows":
    requires += [
        'WMI',
        'PIL',
        'pywin32',
    ]
elif platform.system() == "Darwin":
    scripts += [
        'bin/pyfetch_macosx_defbrowser',
    ]

setup(
    name='pyFetch',
    version=pyFetch.version,
    description='Python system fetching information tool',
    author='Tedley Meralus',
    author_email='tmeralus@gmail.com',
    url='https://github.com/tedleyem/pyFetch',
    packages=['pyFetch'],
    requires = ['colorama'],
    scripts = ['bin/pyfetch']
)