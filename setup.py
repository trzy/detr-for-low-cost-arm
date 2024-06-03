from distutils.core import setup
from setuptools import find_packages

setup(
    name='detr',
    version='0.0.2',
    packages=find_packages(),
    url="https://github.com/trzy/detr-for-low-cost-robot-arm",
    license='MIT License',
    long_description=open('README.md').read(),
)
