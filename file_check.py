#!/usr/bin/env python

import os

def verify_file(resource) -> bool:

    if os.path.isfile(resource) and os.access(resource, os.R_OK):
        """checks to see if file exists and is readable"""
        return True
    return False