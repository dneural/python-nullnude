Python SDK for NullNude API
===========================

This is a Python SDK to use Nudity detection and automatic moderate features from 
[NullNude](https://nullnude.com). The SDK uses the simple API provided by 
NullNude.
Use the NullNude API to instantly moderate adult content in user-submitted photos. 

[![Build 
Status](https://travis-ci.org/dneural/python-nullnude.svg?branch=master)](https://travis-ci.org/dneural/python-nullnude)
[![Coverage 
Status](https://coveralls.io/repos/dneural/python-nullnude/badge.png?branch=master)](https://coveralls.io/d/dneural/python-nullnude?branch=master)

Quickstart
----------

The easiest way to start with the SDK is to install it from PyPi:

    pip install python-nullnude

NullNude SDK can then be included in your Python programs. Some examples of
applications using the SDK are available in the `examples` directory.

Install from source
-------------------

To install the SDK from the Github sources you have to clone the repository.
Then, you can install the SDK with:

    python setup.py install


Authenticate to NullNude API
----------------------------

Each **application** that uses NullNude API needs to be authenticated. For that 
you have to register your application, it is very easy and can be done at this 
address: https://nullnude.com/register


How to check photos for nudity content?
---------------------------------------

Checking photo for nudity is easy. Provide URL or local file and call 
`nullnude.nudity.check(image)`. To retrieve ROI that contains nudity content
just call `nullnude.roi.get()` method:

```python
from nullnude import Nullnude

api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Create the NullNude SDK interface
client = Nullnude(api_key, api_secret)

# URL to check for nudity
url = 'https://nullnude.com/wp-content/uploads/2016/01/vintage_porn_1.jpg',

# Check for nudity
ret = nullnude.nudity.check(url)

# is nudity detected ?
is_nudity = ret.nudity

if is_nudity:
    print ('Nudity detected on %s' % url)
    print ('Nudity confidence: %f' % ret.nudity_confidence)

```

How to get ROIs from photo?
-------------------
Region of interests are parts of photo that contains nudity. You can use this method
to moderate photos on your own.


```python
from nullnude import Nullnude

api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Create the NullNude SDK interface
client = Nullnude(api_key, api_secret)

# URL to check for nudity
url = 'https://nullnude.com/wp-content/uploads/2016/01/vintage_porn_1.jpg',

# Fetch nudity ROI 
roi_list = nullnude.roi.get(url)
    
# List ROI
print 'ROI:'
for i in roi_list:
    print (' - Category: %s, roi: %s' % (i.category, i.rect))
    

```

How to build the documentation?
-------------------------------

Documentation is based on sphinx. If you have not already installed sphinx, you 
can install it on your virtualenv:

    pip install sphinx

To generate the documentation in the `doc/build` directory, it's possible to 
use directly:

    python setup.py build_sphinx

How to run tests?
-----------------

To run tests, you need to install some dependencies:

    pip install -r test-requirements.txt

Then, you can directly run the unit tests

    python setup.py test

License
-------

The SDK code is released under a MIT style license, which means that it should 
be easy to integrate it to your application.  
Check the [LICENSE](LICENSE) file for more information.
