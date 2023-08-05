#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This setup.py file was originally templated from https://github.com/navdeep-G/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import fileinput
import glob
import io
import os
import sys
from shutil import rmtree
import atexit
import datetime
from subprocess import Popen, PIPE


import setuptools

# import site
from pip._internal.utils import misc
from setuptools.command.install import install

NAME = "conductor.maya"
DESCRIPTION = "Maya plugin for Conductor Cloud Rendering Platform."
URL = "https://github.com/AtomicConductor/conductor-maya"
EMAIL = "info@conductortech.com"
AUTHOR = "conductor"
REQUIRES_PYTHON = "~=2.7"
VERSION = ""  # version will be populated by __version__.py file


# Very important to change this if you req1uire updated functionality in core.
REQUIRED = ["conductor.core>=0.1.2,<1.0.0"]

# Optional packages/functionality
EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except IOError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_").replace(".", os.sep)
    with open(os.path.join(here, "src", project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(setuptools.Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution…")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system('twine upload --repository-url "https://test.pypi.org/legacy" dist/*')

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
    ],
    cmdclass={"upload": UploadCommand},
    description=DESCRIPTION,
    extras_require=EXTRAS,
    install_requires=REQUIRED,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name=NAME,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    version=about["__version__"],
    zip_safe=False,
    entry_points={"console_scripts": ["setup_maya=conductor.maya.cli.setup_maya:main"]},
    package_data={NAME: ["plug-ins/*.*", "icons/*.*", "scripts/*.*"]},
)
