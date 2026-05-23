#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevMetrics-CLI Setup
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding='utf-8') if readme_path.exists() else ""

setup(
    name="devmetrics-cli",
    version="1.0.0",
    author="DevMetrics Team",
    author_email="dev@devmetrics.io",
    description="轻量级开发者代码度量与生产力分析引擎",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/devmetrics-cli",
    py_modules=["devmetrics"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "devmetrics=devmetrics:main",
            "dm=devmetrics:main",
        ],
    },
    keywords="git metrics productivity developer statistics analysis cli",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/devmetrics-cli/issues",
        "Source": "https://github.com/yourusername/devmetrics-cli",
    },
)
