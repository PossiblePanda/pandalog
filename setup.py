from setuptools import find_packages, setup

setup(
    name='pandalog',
    packages=find_packages(include=['pandalog']),
    version='1.0.0',
    description='A simple library for logging in Python',
    author='Possible Panda',
	install_requires=[],
	setup_requires=['pytest-runner'],
	tests_require=['pytest'],
	test_suite='tests',
)