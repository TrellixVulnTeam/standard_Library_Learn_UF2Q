import base64
import hashlib
import hmac

with open('lorem.txt', 'rb') as f:
    body = f.read()

hash = hmac.new(b'secret key goes here',
                body,
                hashlib.sha1,
                )

digest = hash.digest()
print(base64.encodebytes(digest))
