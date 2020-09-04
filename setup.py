from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='frame_generator',
   version='1.0',
   description='A module to easily read frames from from a vide and display useful video informations.',
   license="MIT",
   long_description=long_description,
   author='Tamás Süveges',
   author_email='stamas01@gmail.com',
   packages=['frame_generator'],
   install_requires=['opencv-python', 'tabulate'],

)
