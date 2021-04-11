from flask import Flask, jsonify, request, g
from common.exceptions import HttpException
from common.decorators import login_required
from service import GymService
import common.utils as u
import os


app = Flask(__name__)
gym_svc = GymService()
auth_util = u.AuthorizationUtils(os.getenv('SECRET_KEY'))

@app.route('/gyms/<gym_id>', methods=['GET'])
@login_required
def get_gym_by_id(gym_id):
    gym = gym_svc.get_by_id(gym_id)
    if gym == None:
        raise HttpException(404)
    return jsonify(gym)

@app.route('/gyms', methods=['GET'])
@login_required
def get_gyms():
    gyms = gym_svc.get_all_gyms()
    return jsonify(content=gyms)

@app.route('/gyms', methods=['POST'])
@login_required
def create_gym():
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['name', 'size'])
    gym = gym_svc.create_gym(data)
    return jsonify(gym)

@app.route('/gyms/<gym_id>', methods=['PUT'])
@login_required
def update_gym(gym_id):
    data = request.get_json()
    u.ValidationUtils.validate_required_fields(data, ['gym_id'])
    updated_gym = gym_svc.update_gym(data)
    return jsonify(updated_gym)

@app.route('/gyms/<gym_id>', methods=['DELETE'])
@login_required
def delete_gym(gym_id):
    deleted = gym_svc.delete_gym(gym_id)
    return jsonify(result=deleted)

@app.errorhandler(HttpException)
def handle_bad_request(e):
    return jsonify(code=e.http_code, info=e.info_msg), e.http_code

# We only need this for local development.
if __name__ == '__main__':
    app.run()
