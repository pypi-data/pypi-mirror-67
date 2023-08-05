
from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Auto-process",
    version="1.0.0",
    description="A Python package to get auto preprocess data.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/roshanfande/Auto-process",
    author="Roshan Fande",
    
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Auto_process"],
    include_package_data=True,
    #install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "Auto-process=Auto_process.Auto_python:main",
        ]
    },
)