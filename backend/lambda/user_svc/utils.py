from functools import wraps
from flask import g, request, redirect, url_for
from exception import HttpException
import jwt
import datetime

"""Decorator
Checks if user is logged in
"""
def login_required(token_svc):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                raise HttpException(403, 'Please provide Authorization token')
            token = request.headers['Authorization']
            user_id = token_svc.decode(token)
            if user_id is None:
                raise HttpException(400, 'Could not decode token')
            g.user_id = user_id
            return function(*args, **kwargs)
        return wrapper
    return decorator

"""
Validation utils, mighe be moved to separate file `validator.py`
"""
class ValidationUtils():

    def __init__(self):
        pass

    @staticmethod
    def validate_required_fields(data, required_fields: []):
        if data is None:
            raise HttpException(400, 'Request data must be present')
        for req_field in required_fields:
            if req_field not in data:
                raise HttpException(400, f'Field {req_field} must be present')

"""
Jwt Token utilities
"""
class TokenSvc():

    def __init__(self, secret_key, expiration_time_millis=60*60*1000):
        self.secret_key = secret_key
        self.expiration_time_millis = expiration_time_millis

    def encode(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(milliseconds=self.expiration_time_millis),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload, self.secret_key, algorithm='HS256')
        except Exception as e:
            raise HttpException(500, f'Could not encode token')
    
    def decode(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HttpException(401, 'Token expired')
        except jwt.InvalidTokenError:
            raise HttpException(401, 'Token invalid')
