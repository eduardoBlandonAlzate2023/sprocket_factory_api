import os
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate_error()
        return f(*args, **kws)

    return decorated_function


def check_auth(username, password):
    admin_username = os.getenv(
        "ADMIN_USERNAME", "admin"
    )
    admin_password = os.getenv(
        "ADMIN_PASSWORD", "password"
    )
    return username == admin_username and password == admin_password


def authenticate_error():
    message = {"error": "Authentication required."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
    return resp
