import pathlib
import os
import codecs
import re
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="modelbase",
    version=find_version("modelbase", "__init__.py"),
    description="A package to build metabolic models",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ebenhoeh/modelbase",
    author="Oliver Ebenhoeh",
    author_email="oliver.ebenhoeh@hhu.de",
    license="GPL3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="modelling ode pde metabolic",
    project_urls={
        "Documentation": "https://modelbase.readthedocs.io/en/latest/",
        "Source": "https://gitlab.com/ebenhoeh/modelbase",
        "Tracker": "https://gitlab.com/ebenhoeh/modelbase/issues",
    },
    packages=find_packages("."),
    install_requires=[
        "numpy>=1.16",
        "scipy",
        "matplotlib>=3.0.3",
        "pandas",
        "python-libsbml",
        "dataclasses",
        "coverage",
        "black",
    ],
    python_requires=">=3.6.0",
    zip_safe=False,
)
