
# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

"""
Sportradar APIs library
"""
__version__ = '1.6.0'
__author__ = 'John W. Miller'
__description__ = 'A Python wrapper for the Sportradar APIs'
__license__ = 'MIT'

import sys
assert sys.version_info[0] == 3, 'The Sportradar API requires Python 3.'
from .api import API
