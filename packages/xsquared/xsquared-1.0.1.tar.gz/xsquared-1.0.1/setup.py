from setuptools import setup, find_packages

setup(
    name='xsquared',
    version='1.0.1',
    packages=find_packages(exclude=['.github*']),
    license='MIT',
    description='a python package that squares its imput',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/gubareve/x-squared/',
    author='Evan Gubarev',
    author_email='evan@evangubarev.com'
)
