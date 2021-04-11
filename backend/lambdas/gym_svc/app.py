from flask import Flask, jsonify, request, g
from common.exceptions import HttpException
from common.decorators import login_required
import common.utils as u
import os


app = Flask(__name__)
auth_util = u.AuthorizationUtils(os.getenv('SECRET_KEY'))

@app.route('/gyms/<gym_id>', methods=['GET'])
@login_required
def get_gym_by_id(gym_id):
    return jsonify(response=f'get gym {gym_id}')

@app.route('/gyms', methods=['GET'])
@login_required
def get_gyms():
    return jsonify(response='get all gyms')

@app.route('/gyms', methods=['POST'])
@login_required
def create_gym():
    data = request.get_json()
    return jsonify(response=f'create: {data}')

@app.route('/gyms/<gym_id>', methods=['PUT'])
@login_required
def update_gym(gym_id):
    data = request.get_json()
    return jsonify(response=f'update gym {data}')

@app.route('/gyms/<gym_id>', methods=['DELETE'])
@login_required
def delete_gym(gym_id):
    return jsonify(response=f'delete gym {gym_id}')

@app.errorhandler(HttpException)
def handle_bad_request(e):
    return jsonify(code=e.http_code, info=e.info_msg), e.http_code

# We only need this for local development.
if __name__ == '__main__':
    app.run()
