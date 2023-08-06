# -*- coding:utf-8 -*-
"""Provides authentification and row access to Cozytouch modules."""
name = "cozytouchpy"
__version__ = "1.5.6"

from .client import CozytouchClient
from .exception import CozytouchException, CozytouchAuthentificationFailed
