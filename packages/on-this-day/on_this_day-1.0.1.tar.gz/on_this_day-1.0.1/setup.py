 
"""Setup script for On This Day Package"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="on_this_day",
    version="1.0.1",
    description="What happened on this day on the past",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thevirusx3/on-this-day",
    author="Saroj Bhattarai",
    author_email="sarojbhattarai2053@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["on_this_day"],
    include_package_data=True,
    install_requires=[
        "beautifulsoup4", "requests"
    ],
    entry_points={"console_scripts": ["thisday=on_this_day.__main__:main"]},
)
