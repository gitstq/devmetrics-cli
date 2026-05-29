#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevMetrics-CLI Setup Script
"""

from setuptools import setup, find_packages
import os

# 读取README
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = ''
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='devmetrics-cli',
    version='1.0.0',
    description='轻量级开发者生产力指标追踪与分析引擎',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='DevMetrics Team',
    author_email='dev@devmetrics.io',
    url='https://github.com/gitstq/DevMetrics-CLI',
    py_modules=['devmetrics'],
    entry_points={
        'console_scripts': [
            'devmetrics=devmetrics:main',
            'dm=devmetrics:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    keywords='developer productivity metrics git analysis cli dashboard',
    python_requires='>=3.7',
    license='MIT',
    zip_safe=False,
)
