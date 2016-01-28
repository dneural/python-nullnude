Nudity and ROI
==============

This is an example application of NullNude nudity detection with the Python SDK.
Checking photo for nudity is easy. Provide URL or local file and call
`nullnude.nudity.check(image)`. To retrieve ROI that contains nudity content
just call `nullnude.roi.get()` method.

How to run it on Debian/Ubuntu?
--------------------------------

First make sure that you installed the NullNude Python SDK on your machine.  
Then you can install the requirements used by the example application.

In the file `nudity.py` you must put your api key and api secret key
which are the credentials needed to access your NullNude account from the API.

You can launch the demo from command line:

```bash
python nudity.py
```
