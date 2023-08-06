# coding:utf-8
import os
from setuptools import find_packages, setup

 
README = "no"

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='admin_city',
    version='1.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A city selector for django xadmin',
    long_description="A xadmin city selector",
    url='https://www.example.com/',
    author='wp',
    author_email='wpsmoly@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)