import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pbitcoin",
    version="0.0.1",
    author="Soobokjin",
    author_email="thdnthdn24@gmail.com",
    description=("Examples"),
    license="BSD",
    keywords="example documentation tutorial",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
