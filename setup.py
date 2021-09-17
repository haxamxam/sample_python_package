import setuptools

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='example_package',
   version='0.0.1',
   description='A useful module',
   license="MIT",
   long_description='long description',
   author='Hamza Suhail',
   author_email='foomail@foo.com',
   url="https://github.com/haxamxam/testPackage",
   packages=['example_package'],  #same as name
)
