import hashlib

to_hash = "securityonion-2.3.200-20230113.iso"

check_sums = {
    "MD5": {
    "check": "70291FFE925E2751559589E749B12164", 
    "sum": "",
    },
    "SHA1": {
    "check": "EFD3C7BA6F4EF6774F4F18ECD667A13F7FDF5CFF", 
    "sum": "",
    },
    "SHA256": {
    "check": "7794C1325F9B72856FC2A47691F7E0292CA28976711A18F550163E3B58E7A401", 
    "sum": "",
    },
}

def hash(algorithm, hash_this):
    with open(hash_this, 'rb') as f:
        digest = hashlib.file_digest(f, algorithm)
        for chunk in iter(lambda: f.read(4096), b""):
            digest.update(chunk)
    hash = str(digest.hexdigest()).upper()
    print("{} Hash:     {}".format(algorithm.upper(), hash))
    for k,v in check_sums.items():
        if k == algorithm.upper():
            v["sum"] = hash
            print("{} Checksum: {}".format(k, v["check"]))

def main():
    for k,v in check_sums.items():
        hash(k.lower(), to_hash)
        if v["check"] == v["sum"]:
            print("{} Checksum: PASSED".format(k))
        else:
            print("{} Checksum: FAILED".format(k))


if __name__ == "__main__":
    main()
