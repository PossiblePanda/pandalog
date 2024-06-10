from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='pandalog',
    packages=find_packages(include=['pandalog']),
    version='1.0.0',
    description='A simple library for logging in Python',
    author='Possible Panda',
	classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PossiblePanda/pandalog",
    install_requires=["colorama"],
)