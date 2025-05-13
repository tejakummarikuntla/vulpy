#!/usr/bin/env python3

import shlex
import subprocess

def run_command(command):
    try:
        process = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

```

import sys

program = sys.argv[1]
username = sys.argv[2]

passwords = [
    '1',
    '12',
    '123',
    '1234',
    '12345',
    '123456',
    '12345678',
    '123123123',
]

for password in passwords:
    result = subprocess.run([program, username, password], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print("cracked! user: {} password: {}".format(username, password))
        break

