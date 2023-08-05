from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='validdocbr',  
     version='1.0.0',
     scripts=['validdocbr'] ,
     author="johnchinaski",
     author_email="tatophoenix666@gmail.com",
     description="Brazilian document validator (CPF or CNPJ) using the check digit",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/JohnChinaski/validdocbr",
     packages=find_packages(),
     zip_safe = False,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )