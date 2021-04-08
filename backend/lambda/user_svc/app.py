from flask import Flask, jsonify, request, g
from exception import HttpException
import utils as u
from service import UserService
import os


app = Flask(__name__)
token_svc = u.TokenSvc(os.getenv('SECRET_KEY'))
user_svc = UserService()

@app.route('/users/register', methods=['POST'])
def register():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['email', 'password'])
    if user_svc.get_by_email(data['email']) is not None:
        raise HttpException(400, f"User with email: {data['email']} already exists")
    user = user_svc.create_user(data)
    return jsonify(user)

@app.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['email', 'password'])
    user = user_svc.get_by_email(data['email'])
    if user is None:
        raise HttpException(404, f'User with email: {data["email"]} not found')
    if user['password'] != data['password']:
        print(f"Error in auth: {data['email']}. DB[{user['password']}] != JS[{data['password']}]")
        raise HttpException(401, 'Passwords not matching')
    result_token = token_svc.encode(user['user_id'])
    print(f"[OK] -- Login as user id: {user['user_id']}, email: {user['email']}")
    return jsonify(token=result_token)

@app.route('/users/me', methods=['GET'])
@u.login_required(token_svc)
def get_curent_user():
    print(f'Instance of: {g.user_id}')
    user = user_svc.get_by_id(g.user_id)
    return jsonify(user)

@app.errorhandler(HttpException)
def handle_bad_request(e):
    return jsonify(code=e.http_code, info=e.info_msg), e.http_code

# We only need this for local development.
if __name__ == '__main__':
    app.run()
