from setuptools import setup, find_packages

pandalog_version = '1.0.1'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pandalog',
    packages=find_packages(include=['pandalog']),
    version=pandalog_version,
    description='A simple library for logging in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Possible Panda',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    package_data={"pandalog": ["VERSION"]},
)