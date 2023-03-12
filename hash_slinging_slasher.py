#!/usr/bin/env python

import hashlib

algorithm = "sha256"

def hash_check(is_hash) -> bool:
    try:
        hashlib.sha256(is_hash)
        return True
    except:
        print("\nPlease enter a valid sha256 check sum:\n\n")
        return False
   
def hash_it(hash_this, check_sum) -> str:
    with open(hash_this, 'rb') as f:
        digest = hashlib.file_digest(f, algorithm)
        for chunk in iter(lambda: f.read(4096), b""):
            digest.update(chunk)
    hash_sum = str(digest.hexdigest()).upper()
    print("{} Checksum: {}".format(algorithm, check_sum.upper()))
    print("{} Hash Sum:     {}".format(algorithm.upper(), hash_sum))
    if hash_sum.upper() == check_sum.upper():
        print("File hash sum and provided check sum match!")
    elif check_sum != '' or check_sum != None:
        print("----> WARNING! <----\nHash sum and Check sum DO NOT MATCH!")
    return hash_sum