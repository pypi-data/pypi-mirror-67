# -*- coding: utf-8 -*-
"""
saltfactories.utils.compat
~~~~~~~~~~~~~~~~~~~~~~~~~~

Imports compatability layer
"""
import sys
import weakref

# pragma: no cover
# pylint: disable=unused-import,invalid-name
try:
    from unittest import mock
except ImportError:
    import mock

if sys.version_info < (3,):
    import backports.weakref

    weakref.finalize = backports.weakref.finalize
# pylint: enable=unused-import,invalid-name
