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

import unittest
import mock

import nullnude

class TestNullnude(unittest.TestCase):

    application_key = 'test_api_key'
    application_secret = 'test_api_secret'

    @mock.patch('nullnude.wrapper_api')
    def setUp(self, mock_wrapper):
        self.mock_wrapper = mock_wrapper
        self.client = nullnude.Nullnude(self.application_key,
                                        self.application_secret)
        self.client._api = self.mock_wrapper

    def test_existance_of_nudity_manager(self):
        manager = self.client.nudity
        self.assertIsInstance(manager, nullnude.nudity.NudityManager)

    def test_existance_of_roi_manager(self):
        manager = self.client.roi
        self.assertIsInstance(manager, nullnude.roi.RoiManager)

    def test_existance_of_moderate_manager(self):
        service = self.client.moderate
        self.assertIsInstance(service, nullnude.moderate.ModerateManager)

if __name__ == '__main__':
    unittest.main()
