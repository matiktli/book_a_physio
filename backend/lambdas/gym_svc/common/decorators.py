from .exceptions import HttpException
from .utils import AuthorizationUtils
from flask import g, request
from functools import wraps
import os
import requests

def __do_auth_via_util(token):
    return AuthorizationUtils(secret_key=os.getenv('SECRET_KEY')).decode(token)

def __do_auth_via_security_svc(token):
    authorize_url = os.getenv('USER_SVC_PATH') + '/users/authorize' + '?token=' + token
    r = requests.get(authorize_url)
    if r.status_code != 200:
        return None
    return r.json()['user_id']

def __authorize(request_obj, global_variables, auth_action='service'):
    if 'Authorization' not in request_obj.headers:
        raise HttpException(403, 'Please provide Authorization token')
    token = request_obj.headers['Authorization']
    if auth_action == 'service':
        user_id = __do_auth_via_security_svc(token)
    else:
        user_id = __do_auth_via_util(token)
    if user_id is None:
        raise HttpException(400, 'Could not decode token')
    global_variables.user_id = user_id
    
"""Decorator
Checks if user is logged in
"""
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __authorize(request, g)
        return func(*args, **kwargs)
    return wrapper