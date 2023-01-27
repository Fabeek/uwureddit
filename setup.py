# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="uwureddit",
    version="0.1",
    description="uwureddit is a Python library for accessing the Reddit API. It allows developers to easily interact with the REST API to retrieve and update data on the Reddit website. The library provides a simple and easy-to-use interface for accessing the various endpoints of the API, such as fetching posts, comments, and user information. uwureddit also supports OAuth2 authentication, which allows users to access private data and perform actions such as posting and commenting on the website. The library is actively maintained by developers and used to make Reddit-based apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fabeek/uwureddit.git",
    author="Fabeek",
    author_email="fabien.nicou@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["uwureddit"],
    include_package_data=True,
)
