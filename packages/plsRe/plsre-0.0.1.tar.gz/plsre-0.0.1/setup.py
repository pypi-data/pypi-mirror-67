import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="plsre",
	version="0.0.1",
	author="Charles Chen",
	author_email = "yc414@duke.edu",
	description="A simple package for Partial Least-Sqaures Regression",
	long_description=long_description,
	long_description_content_type = "text/markdown",
	url="https://github.com/ychen381/PLSR",
	keywords = 'package models regression',
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent"
	],
	)
