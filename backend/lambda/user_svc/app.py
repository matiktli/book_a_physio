from flask import Flask, jsonify, request, g
from exception import HttpException
import utils as u
from service import UserService
import os

app = Flask(__name__)
token_utils = u.TokenUtils(os.getenv('SECRET_KEY'))
user_svc = UserService()


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['email', 'password'])
    if user_svc.find_by_email(data['email']) is not None:
        raise HttpException(400, f"User with email: {data['email']} already exists")
    user = user_svc.create_user(data)
    return jsonify(user)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['email', 'password'])
    return jsonify(token='my-token-here')

@app.route('/me', methods=['GET'])
def get_curent_user():
    return jsonify(user_svc.get_all_users())

@app.errorhandler(HttpException)
def handle_bad_request(e):
    return jsonify(code=e.http_code, info=e.info_msg), e.http_code

# We only need this for local development.
if __name__ == '__main__':
    app.run()
