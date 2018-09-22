# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

import re
import os
from setuptools import find_packages, setup

VERSIONFILE = "sportradar/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in {}".format(VERSIONFILE))

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(name="sportradar",
      version=version,
      description="A Python wrapper for the Sportradar APIs",
      long_description=README,
      long_description_content_type="text/markdown",
      license="MIT",
      author="John W. Miller",
      url="https://github.com/johnwmillr/SportradarAPIs",
      packages=find_packages(exclude=['tests']),
      install_requires=["requests"],
      keywords="sportsradar API sports basketball NBA football NFL soccer",
      python_requires=">=3.*",
      classifiers=[
              'Topic :: Software Development :: Libraries',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ])
