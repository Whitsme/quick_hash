#!/usr/bin/env python

import urllib.request

def verify_url(resource):
    try:
        r = urllib.request.urlopen(resource).getcode()
        """checks to see if url returns a OK status code"""
        if r < 400:
            return True
        return False
    except:
        return False