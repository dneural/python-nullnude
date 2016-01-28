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

"""NullNude ROI service library."""
from __future__ import absolute_import

from .base import BaseManager


class RoiManager(BaseManager):
    """Check nudity content using NullNude."""

    method = '/roi.json'

    categories = {
        'n00000001': 'Rear',
        'n00000002': 'Breasts',
        'n00000003': 'Penis',
        'n00000004': 'Female crotch',
        'n00000005': 'Foot',
        'n00000006': 'Stockings',
        'n00000007': 'Bondage',
        'n00000008': 'Dildo',
        'n00000009': 'Fellatio',
        'n00000010': 'Intercourse',
        'n00000011': 'Breast',
        'n00000012': 'Stocking',
        'n00000013': 'Feet',
        'n00000014': 'Anus',
        'n00000015': 'Naked leg',
        'n00000016': 'Naked legs',
        'n00000017': 'Cunnilingus',
        'n00000018': 'Masturbation',
        'n00000019': 'Nipple',
        'n00000020': 'Sperm',
        'n00000021': 'Vagina',
        'n00000022': 'Stocking band',
        'n00000023': 'Underwear',
        'n00000024': 'Bra',
        'n00000025': 'Mouth',
        'n00000026': 'Belly button',
    }

    def get(self, image):
        url = self._handler.endpoint + self.method
        roi = self._api.call_api(url, image)
        return self._dict_to_obj(roi)

    def _dict_to_obj(self, response):
        """Converts dict to an NudityCheck object.
        """

        data = response.get('data')

        roi = data.get('roi')
        url = data.get('url')

        roi_collection = []
        for r in roi:
            category = self.categories.get(r.get('category'))
            rect = (r.get('x1'), r.get('y1'), r.get('x2'), r.get('y2'))
            roi_obj = NudityRoi(self, url, category, rect)
            roi_collection.append(roi_obj)

        return roi_collection


class NudityRoi(object):
    """Represents one nudity ROI result."""

    def __init__(self, manager, url, category, rect):

        self._manager = manager
        self._url = url
        self._category = category
        self._x1, self._y1, self._x2, self._y2 = rect

    @property
    def category(self):
        """Detected category of this ROI"""
        if self._category is False:
            return None

        return self._category

    @property
    def x1(self):
        """x1 Point of this ROI"""
        if self._x1 is False:
            return None

        return self._x1

    @property
    def y1(self):
        """y1 Point of this ROI"""
        if self._y1 is False:
            return None

        return self._y1

    @property
    def x2(self):
        """x2 Point of this ROI"""
        if self._x2 is False:
            return None

        return self._x2

    @property
    def y2(self):
        """y2 Point of this ROI"""
        if self._y2 is False:
            return None

        return self._y2

    @property
    def url(self):
        """Get url of tested image"""
        if self._url is False:
            return None

        return self._url

    @property
    def rect(self):
        """Get rect of this ROI"""
        return self.x1, self.y1, self.x2, self.y2
