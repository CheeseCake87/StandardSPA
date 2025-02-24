from flask import render_template, session, redirect, url_for
from flask_imp.security import checkpoint

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    return render_template(bp.tmpl("index.html"))

@bp.route("/task", methods=["GET"])
def start_task():
    from app.scheduler import manual_task

    manual_task()
    return "task started"

@bp.get("/login")
def login():
    session["auth"] = True
    return redirect(url_for('testing.index'))


@bp.get("/logout")
def logout():
    session["auth"] = False
    return redirect(url_for('testing.index'))


@bp.get("/auth")
@checkpoint("auth", True, fail_endpoint='testing.auth_error')
def auth():
    return redirect(url_for('testing.index'))


@bp.get("/auth-error")
def auth_error():
    return "You are not logged in."
