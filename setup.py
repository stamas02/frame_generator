from setuptools import setup



with open("README.md", 'r') as f:
    long_description = f.read()
long_description_content_type = "text/markdown"


setup(
   name='frame_generator',
   version='1.0',
   description='A module to easily read frames from from a vide and display useful video information.',
   license="MIT",
   keywords = ['vide', 'frame', 'frame-reader'],
   long_description=long_description,
   author='Tamas Suveges',
   url = 'https://github.com/stamas02/frame_generator',
   author_email='stamas01@gmail.com',
   packages=['frame_generator'],
   install_requires=['opencv-python', 'tabulate'],
   classifiers=[
      'Development Status :: 4 - Beta',
      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
      'Intended Audience :: Developers',  # Define that your audience are developers
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',  # Again, pick a license
      'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
   ],
)
