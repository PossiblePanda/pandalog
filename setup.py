from setuptools import find_packages, setup
import subprocess

cf_remote_version = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in cf_remote_version, "Version number is not in the correct format"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='pandalog',
    packages=find_packages(include=['pandalog']),
    version=cf_remote_version,
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