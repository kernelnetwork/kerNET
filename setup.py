import os
from setuptools import setup, find_packages

setup(
    name='kernet',
    version="0.1.1",
    author="anonymous",
    description=("Code for paper: 'Learning Backpropagation-Free Deep Architectures with Kernels.'"),
    license="MIT",
    url="https://github.com/kernelnetwork/kerNET",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='utf-8').read(),
    packages=find_packages(),
)