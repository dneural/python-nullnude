#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2015, dNeural.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Except as contained in this notice, the name of dNeural and or its trademarks
# (and among others NullNude) shall not be used in advertising or otherwise to
# promote the sale, use or other dealings in this Software without prior
# written authorization from dNeural.

"""NullNude SDK interface for users."""
from __future__ import absolute_import

from .wrapper_api import WrapperApi
from .nudity import NudityManager
from .roi import RoiManager
from .moderate import ModerateManager


class Nullnude(object):
    """SDK interface to get cloud services from NullNude."""

    def __init__(self, api_key, api_secret):
        """Create the main interface of the SDK.

        :param api_key: API key of your NullNude account
        :param api_secret: API secret of your NullNude account
        """
        self.endpoint = 'https://api.dneural.com/1.0'

        self._api = WrapperApi(api_key, api_secret)
        self.nudity = NudityManager(self._api, self)
        self.roi = RoiManager(self._api, self)
        self.moderate = ModerateManager(self._api, self)
