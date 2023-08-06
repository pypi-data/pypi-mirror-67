from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='patient1',  
     version='0.0.1',
     description='simple example',
     long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/Renuga349/patient1",
   author="renuga",
     author_email="renugadevi22111997@gmail.com",
   py_modules=["patient1"],
 )