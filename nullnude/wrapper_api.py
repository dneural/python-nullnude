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

"""
This module provides a simple python wrapper over the NullNude API
"""
from __future__ import absolute_import

import requests
import json

from .exception import APIError


class WrapperApi(object):
    """Simple wrapper class for NullNude API."""

    base_url = 'https://api.dneural.com/1.0'

    def __init__(self, api_key, api_secret):
        """Create the main interface of the SDK.

        :param api_key: API key of your NullNude account
        :param api_secret: API secret of your NullNude account
        """
        self._api_key = api_key
        self._api_secret = api_secret
        self._endpoint = 'https://api.dneural.com/1.0'

    @property
    def api_key(self):
        return self._api_key

    @property
    def api_secret(self):
        return self._api_secret

    def call_api(self, api_url, image):
        """Call remote API and return its result.
        :param api_url: the url you want to request
        :param image: the object you want to send in your request

        :raises APIError: Error send by api
        """
        data = {
            'api_key': self._api_key,
            'api_secret': self._api_secret
        }

        if any(x in image.lower() for x in ('http://', 'https://')):
            data.update({'url': image})
            r = requests.get(api_url, data=data)
        else:
            r = requests.post(api_url, files={'photo': open(image, 'rb')}, data=data)

        try:
            retval = json.loads(r.text)
        except ValueError:
            raise APIError('API response is not valid')

        if r.status_code < 100 or r.status_code >= 300:
            raise APIError(msg=retval.get('error_message'))

        return retval
