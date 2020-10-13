import sys
import hashlib

lastDigits = "34623251"
name = b"jonatbr"

for l in sys.stdin:
    extra = l.strip("\n").encode("utf-8")
    h = hashlib.sha256(name + extra).hexdigest()
    if lastDigits == h[-8:]:
        print(extra)
        print(h)
        break