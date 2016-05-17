import os
import sys
from   setuptools import setup, find_packages
from   setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


#class PyTest(TestCommand):
#    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

#    def initialize_options(self):
#        TestCommand.initialize_options(self)
#        self.pytest_args = []

#    def finalize_options(self):
#        TestCommand.finalize_options(self)
#        self.test_args = []
#        self.test_suite = True

#    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
#        import pytest
#        errno = pytest.main(self.pytest_args)
#        sys.exit(errno)


setup(
    name="",
    version="0.1.0",
    author="Oier Echaniz",
    description="Fastq merger",
    license="MIT",
    keywords=[
        "biomerger",
    ],
    url="",
    packages=find_packages(),
    long_description=read('README.md'),
    scripts=['scripts/biomerger'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    #test requirements and class specification:
    #tests_require=['pytest'],
    #cmdclass={ 'test' : PyTest },
)
