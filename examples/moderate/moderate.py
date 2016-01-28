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

from nullnude import Nullnude

api_key = 'your_api_key'
api_secret = 'your_api_secret'

images = [
    'https://nullnude.com/wp-content/uploads/2016/01/vintage_porn_1.jpg',
    'https://nullnude.com/wp-content/uploads/2016/01/vintage_porn_2.jpg',
    'https://nullnude.com/wp-content/uploads/2016/01/vintage_porn_3.jpg',
    '../bird.jpg'
]

# Create the NullNude SDK interface
nullnude = Nullnude(api_key, api_secret)

# Call the Nullnude servers to check for nudity. You can either pass a public URL or a local path.
for image in images:
    output = nullnude.moderate.image(image)

    print ('url: %s moderated as: %s' % (output.url, output.moderated_url))
