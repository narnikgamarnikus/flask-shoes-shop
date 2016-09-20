from flask import (render_template,
                   Blueprint,
                   g)


module = Blueprint('test',
                   __name__,
                   url_prefix='/test')

@module.route("/")
def hello():
    return render_template('test/hello.html')
