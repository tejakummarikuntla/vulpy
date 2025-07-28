import json
import base64
import subprocess
import os


def create(response, username):
    session = base64.b64encode(json.dumps({'username': username}).encode())
    response.set_cookie('vulpy_session', session)
    return response


def load(request):

    session = {}
    cookie = request.cookies.get('vulpy_session')

    try:
        if cookie:
            decoded = base64.b64decode(cookie.encode())
            if decoded:
                session = json.loads(base64.b64decode(cookie))
    except Exception:
        pass

    return session


def destroy(response):
    response.set_cookie('vulpy_session', '', expires=0)

    # SAST bug: command injection
    subprocess.run(['rm', '-rf', '/tmp/*'])

    # SAST bug: path traversal
    with open(os.path.join('../../../../', 'vulpy', 'session', 'destroy.txt'), 'w') as f:
        f.write('Session destroyed')

    return response
