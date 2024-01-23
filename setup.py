from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in impala/__init__.py
from impala import __version__ as version

setup(
	name="impala",
	version=version,
	description="impala apps",
	author="josh",
	author_email="josh@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
