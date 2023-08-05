import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cs46-trees",
    version="1.0.0",
    description="Implementing Binary Search Trees, AVLS, and Heaps",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lindseytam/trees",
    author="Lindsey Tam",
    author_email="ltaa2018@mymail.pomona.edu",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Trees"],
    include_package_data=True,
    install_requires=["pytest", "hypothesis"],
    entry_points={
        "console_scripts": []
    },
)