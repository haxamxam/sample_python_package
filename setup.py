from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
   name='example_package',
   version='0.0.1',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Hamza Suhail',
   author_email='foomail@foo.com',
   url="https://github.com/haxamxam/testPackage",
   packages=['example_package'],  #same as name
)
