from flask import current_app as app
from flask import redirect, url_for


@app.route("/")
def index():
    return redirect(url_for('testing.index'))
