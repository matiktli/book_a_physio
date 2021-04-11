from flask import Flask, jsonify, request, g
from common.exceptions import HttpException
from common.decorators import login_required
import common.utils as u
from service import UserService
import os


app = Flask(__name__)
auth_util = u.AuthorizationUtils(os.getenv('SECRET_KEY'))
user_svc = UserService()

def __login(user_data):
    user = user_svc.get_by_email(user_data['email'])
    if user is None:
        raise HttpException(401, f'User with email: {user_data["email"]} not found')
    if user['password'] != user_data['password']:
        raise HttpException(401, 'Passwords not matching')
    return auth_util.encode(user['user_id'])

@app.route('/users/register', methods=['POST'])
def register():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['email', 'password'])
    if user_svc.get_by_email(data['email']) is not None:
        raise HttpException(400, f"User with email: {data['email']} already exists")
    user = user_svc.create_user(data)
    token = __login(data)
    return jsonify(user=user, token=token)

@app.route('/users/authorize', methods=['GET'])
def authorize():
    u.ValidationUtils.validate_required_fields(request.args, ['token'])
    token = request.args.get('token')
    user_id = auth_util.decode(token)
    user = user_svc.get_by_id(user_id)
    return jsonify(user)

@app.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['email', 'password'])
    token = __login(data)
    return jsonify(token=token)

@app.route('/users/<user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['id'])
    updated_user = user_svc.update_user(data)
    return jsonify(updated_user)

@app.route('/users/me', methods=['GET'])
@login_required
def get_curent_user():
    user = user_svc.get_by_id(g.user_id)
    if user == None:
        raise HttpException(404)
    return jsonify(user)

@app.errorhandler(HttpException)
def handle_bad_request(e):
    return jsonify(code=e.http_code, info=e.info_msg), e.http_code

# We only need this for local development.
if __name__ == '__main__':
    app.run()
