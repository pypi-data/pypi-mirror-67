# -*- coding: utf-8 -*-
# Copyright (c) 2020 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

__version__ = "0.5.3"

# from eapi.constants import ENCODING, INCLUDE_TIMESTAMPS, SSL_VERIFY, \
#                          SSL_WARNINGS, TIMEOUT

from eapi.sessions import Session, session
from eapi.api import configure, enable, execute, login, logout, new, close