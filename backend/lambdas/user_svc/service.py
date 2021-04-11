from common.exceptions import HttpException
from dao import User
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserService():
    def __init__(self):
        self.user_dao = User

    def get_all_users(self):
        user_list = self.user_dao.select()
        return [model_to_dict(u) for u in user_list]

    def get_by_email(self, email):
        try:
            return model_to_dict(self.user_dao.get(self.user_dao.email == email))
        except DoesNotExist:
            return None
    
    def get_by_id(self, user_id):
        try:
            return model_to_dict(self.user_dao.get(self.user_dao.user_id == user_id))
        except DoesNotExist:
            return None

    def create_user(self, user_data):
        try:
            return model_to_dict(self.user_dao.create(email=user_data['email'], password=user_data['password']))
        except IntegrityError as e:
            raise HttpException(400, f"Error while creating user with email: {user_data['email']}")
    
    def update_user(self, user_data):
        if 'id' not in user_data:
            raise HttpException(400, 'Could not update user without id provided')
        raise HttpException(501, 'Not implemented')