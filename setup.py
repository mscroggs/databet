"""Databet."""

import os
import sys

import setuptools

import make_letters

if sys.version_info < (3, 6):
    print("Python 3.6 or higher required, please upgrade.")
    sys.exit(1)

make_letters.make()
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.md")) as f:
    long_description = f.read().replace(
        "(img/",
        "(https://raw.githubusercontent.com/mscroggs/databet/main/img/")


data_files = ["LICENSE", "README.md"]

if __name__ == "__main__":
    setuptools.setup(
        name="databet",
        description="datasets with the same summary statistics that look like the alphabet",
        long_description=long_description,
        long_description_content_type="text/markdown",
        version="2023.1.1",
        author="Matthew Scroggs",
        license="MIT",
        author_email="databet@mscroggs.co.uk",
        maintainer_email="databet@mscroggs.co.uk",
        url="https://github.com/mscroggs/databet",
        packages=["databet"],
        package_data={"databet": ["py.typed"]},
        include_package_data=True,
        data_files=data_files,
        install_requires=["numpy", "matplotlib"],
    )
