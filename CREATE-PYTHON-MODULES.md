# creating a python package 
# https://setuptools.pypa.io/en/latest/userguide/quickstart.html
# [PEP 517](https://peps.python.org/pep-0517/)
# [What is setup.py](https://stackoverflow.com/questions/1471994/what-is-setup-py)
# [Installing Python Modules](https://docs.python.org/3/installing/index.html#installing-index)

Using setup.py

Let's start with some definitions:

Package - A folder/directory that contains __init__.py file. Module - A valid python file with .py extension. Distribution - How one package relates to other packages and modules.

Let's say you want to install a package named foo. Then you do,

$ git clone https://github.com/user/foo
$ cd foo
$ python setup.py install
Instead, if you don't want to actually install it but still would like to use it. Then do,

$ python setup.py develop
This command will create symlinks to the source directory within site-packages instead of copying things. Because of this, it is quite fast (particularly for large packages).

Creating setup.py

If you have your package tree like,

foo
├── foo
│   ├── data_struct.py
│   ├── __init__.py
│   └── internals.py
├── README
├── requirements.txt
└── setup.py
Then, you do the following in your setup.py script so that it can be installed on some machine:

from setuptools import setup

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['foo'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)
Instead, if your package tree is more complex like the one below:

foo
├── foo
│   ├── data_struct.py
│   ├── __init__.py
│   └── internals.py
├── README
├── requirements.txt
├── scripts
│   ├── cool
│   └── skype
└── setup.py
Then, your setup.py in this case would be like:

from setuptools import setup

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['foo'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)
Add more stuff to (setup.py) & make it decent:

from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='foomail@foo.example',
   url="http://www.foopackage.example/",
   packages=['foo'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)
The long_description is used in pypi.org as the README description of your package.

And finally, you're now ready to upload your package to PyPi.org so that others can install your package using pip install yourpackage.

At this point there are two options.

publish in the temporary test.pypi.org server to make oneself familiarize with the procedure, and then publish it on the permanent pypi.org server for the public to use your package.
publish straight away on the permanent pypi.org server, if you are already familiar with the procedure and have your user credentials (e.g., username, password, package name)
Once your package name is registered in pypi.org, nobody can claim or use it. Python packaging suggests the twine package for uploading purposes (of your package to PyPi). Thus,

the first step is to locally build the distributions using:

# prereq: wheel (pip install wheel)
$ python setup.py sdist bdist_wheel
then using twine for uploading either to test.pypi.org or pypi.org:

$ twine upload --repository testpypi dist/*
username: ***
password: ***
It will take few minutes for the package to appear on test.pypi.org. Once you're satisfied with it, you can then upload your package to the real & permanent index of pypi.org simply with:

$ twine upload dist/*
Optionally, you can also sign the files in your package with a GPG by:

$ twine upload dist/* --sign
