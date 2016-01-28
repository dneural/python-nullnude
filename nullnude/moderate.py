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

"""NullNude moderate service library."""
from __future__ import absolute_import

from .base import BaseManager


class ModerateManager(BaseManager):
    """Moderate nudity photo using NullNude engine."""

    method = '/moderate.json'

    def image(self, image):

        url = self._handler.endpoint + self.method
        roi = self._api.call_api(url, image)
        return self._dict_to_obj(roi)

    def _dict_to_obj(self, response):
        """Converts dict to an NudityCheck object.

        """
        data = response.get('data')

        url = response.get('url')
        moderated = data.get('moderated')
        is_moderated = moderated.get('result')
        moderated_url = False
        if is_moderated:
            moderated_url = moderated.get('url')

        mod = ModeratedPhoto(self, url, moderated_url)

        return mod


class ModeratedPhoto(object):
    """Represents moderated image result."""

    def __init__(self, manager, url, moderated_url):

        self._manager = manager
        self._url = url
        self._moderated_url = moderated_url

    @property
    def moderated_url(self):
        """Get url of moderated image"""
        if self._moderated_url is False:
            return None

        return self._moderated_url

    @property
    def url(self):
        """Get url of tested image"""
        if self._url is False:
            return None

        return self._url
