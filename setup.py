from setuptools import find_packages, setup
import subprocess
import os

pandalog_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in pandalog_version:
    v,i,s = pandalog_version.split("-")
    pandalog_version = v + "+" + i + ".git." + s

assert "-" not in pandalog_version, "Invalid version string: %s" % pandalog_version
assert "." in pandalog_version, "Invalid version string: %s" % pandalog_version

assert os.path.isfile("pandalog/version.py"), "version.py not found"
with open("pandalog/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % pandalog_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='pandalog',
    packages=find_packages(include=['pandalog']),
    version=pandalog_version,
    description='A simple library for logging in Python',
    author='Possible Panda',
	classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    package_data={"pandalog": ["VERSION"]},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PossiblePanda/pandalog",
    install_requires=["colorama"],
)