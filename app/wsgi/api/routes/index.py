from flask import session
from flask_imp.security import api_checkpoint

from .. import bp


@bp.get("/")
def index():
    return {
        "route": "api.index",
        "auth": session.get("auth")
    }


@bp.get("/clear-session")
def clear_session():
    session.clear()
    return {"route": "api.clear-session"}


@bp.get("/secured")
@api_checkpoint("auth", True, {"error": "You are not logged in."})
def secured():
    return {"route": "api.secured"}


@bp.get("/login")
def login():
    session["auth"] = True
    return {"route": "api.login", "auth": session["auth"]}


@bp.get("/logout")
def logout():
    session["auth"] = False
    return {"route": "api.logout", "auth": session["auth"]}
