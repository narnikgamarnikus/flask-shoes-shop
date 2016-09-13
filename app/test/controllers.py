from flask import (render_template,
                   Blueprint,
                   g)

import flask_sijax

module = Blueprint('test',
                   __name__)

@flask_sijax.route(module, '/')
def index():
    def say_hi(obj_response):
        obj_response.alert('Hi there!')

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()

    return render_template('test/hello.html')