from setuptools import setup
import sys
install_requires = []
python_ver = sys.version_info
if python_ver.major == 2 and python_ver.minor < 7:
    install_requires = ['ordereddict']

setup(name='py-dag',
      version='2.6.1',
      description='Directed acyclic graph implementation',
      url='https://github.com/thieman/py-dag',
      author='Travis Thieman',
      author_email='travis.thieman@gmail.com',
      license='MIT',
      packages=['dag'],
      install_requires=install_requires,
      test_suite='nose.collector',
      tests_require=['nose'] + install_requires,
      zip_safe=False)
