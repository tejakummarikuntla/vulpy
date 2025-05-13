import libuser
import random
import hashlib
import re
import jwt
from time import time

from pathlib import Path

secret = 'MYSUPERSECRETKEY'
not_after = 60 # 1 minute

def keygen(username, password=None, login=True):

    if login:
        if not libuser.login(username, password):
            return None

    now = time()
            import base64
import hashlib
import hmac
import json
import time

def encode_jwt(username, now, not_after, secret):
    payload = {
        'username': username,
        'nbf': now,
        'exp': now + not_after
    }
    encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().replace('=', '')
    header = {'alg': 'HS256', 'typ': 'JWT'}
    encoded_header = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().replace('=', '')
    signature = hmac.new(secret.encode(), (encoded_header + '.' + encoded_payload).encode(), hashlib.sha256).digest()
    encoded_signature = base64.urlsafe_b64encode(signature).decode().replace('=', '')
    return encoded_header + '.' + encoded_payload + '.' + encoded_signature

```


    return token


def authenticate(request):

    if 'authorization' not in request.headers:
        return None

    try:
        authtype, token = request.headers['authorization'].split(' ')
    except Exception as e:
        print(e)
        return None

    if authtype.lower() != 'bearer':
        print('not bearer')
        return None

    try:
        decoded = jwt.decode(token, secret, algorithms=['HS256'])
    except Exception as e:
        print(e)
        return None

    return decoded['username']

