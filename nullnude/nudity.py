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

"""NullNude instance service library."""
from __future__ import absolute_import

from .base import BaseManager


class NudityManager(BaseManager):
    """Check nudity content using NullNude."""

    method = '/nudity.json'

    def check(self, image):

        url = self._handler.endpoint + '/nudity.json'
        nudity = self._api.call_api(url, image)
        return self._dict_to_obj(nudity)

    def _dict_to_obj(self, response):
        """Converts dict to an NudityCheck object.

        """
        data = response.get('data')

        nudity = data.get('nudity').get('result')
        nudity_confidence = data.get('nudity').get('confidence')

        cnudity = data.get('covered_nudity').get('result')
        cnudity_confidence = data.get('covered_nudity').get('confidence')

        url = data.get('url')

        return NudityCheck(self, url, nudity, nudity_confidence, cnudity, cnudity_confidence)


class NudityCheck(object):
    """Represents one nudity check result."""

    def __init__(self, manager, url, nudity, nudity_confidence, covered_nudity,
                 covered_nudity_confidence):

        self._manager = manager
        self._url = url
        self._nudity = nudity
        self._nudity_confidence = nudity_confidence
        self._covered_nudity = covered_nudity
        self._covered_nudity_confidence = covered_nudity_confidence

    @property
    def nudity(self):
        """Nudity in image"""
        return self._nudity

    @property
    def nudity_confidence(self):
        """Confidence of nudity in image"""
        if self._nudity_confidence is False:
            return None

        return self._nudity_confidence

    @property
    def covered_nudity(self):
        """Covered nudity in image"""
        return self._covered_nudity

    @property
    def covered_nudity_confidence(self):
        """Confidence of covered nudity in image"""
        if self._covered_nudity_confidence is False:
            return None

        return self._covered_nudity_confidence

    @property
    def url(self):
        """Get url of tested image"""
        if self._url is False:
            return None

        return self._url
