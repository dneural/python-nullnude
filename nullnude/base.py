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

"""NullNude base class definition library."""


class BaseManager(object):
    """Basic manager type providing common operations.
    Managers interact with a particular NullNude functions.
    """
    def __init__(self, wrapper_api, nullnude_handler):
        """Build a manager with reference to the API.
        :param wrapper_api: client of NullNude API
        :param nullnude_handler: reference to NullNude user interface
        """
        self._api = wrapper_api
        self._handler = nullnude_handler
