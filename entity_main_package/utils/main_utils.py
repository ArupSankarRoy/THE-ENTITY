
# Utils are those functionality that we will be using frequently in our code.
# Insted of writing them in seperate component we write them in main utils,and when ever i need those file we are importing main_utils.

import os.path
import sys
import yaml
import base64

from entity_main_package.exception import AppException
from entity_main_package.logger import logging


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())