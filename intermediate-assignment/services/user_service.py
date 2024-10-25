from functools import wraps
from flask import session, redirect, url_for

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'role' not in session or session['role'].lower() != role.lower():
                return redirect(url_for('user.login', error='Unauthorized'))
            return func(*args, **kwargs)
        return wrapper
    return decorator