from common.exceptions import HttpException
from dao import Gym
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict, dict_to_model

class GymService():
    def __init__(self):
        self.gym_dao = Gym

    def get_all_gyms(self):
        gym_list = self.gym_dao.select()
        return [model_to_dict(u) for u in gym_list]

    def get_by_name(self, name):
        try:
            return model_to_dict(self.gym_dao.get(self.gym_dao.name == name))
        except DoesNotExist:
            return None
    
    def get_by_id(self, gym_id):
        try:
            return model_to_dict(self.gym_dao.get(self.gym_dao.gym_id == gym_id))
        except DoesNotExist:
            return None

    def create_gym(self, gym_data):
        try:
            return model_to_dict(self.gym_dao.create(name=gym_data['name'], size=gym_data['size']))
        except IntegrityError as e:
            raise HttpException(400, f"Error while creating gym with name: {gym_data['name']}")
    
    def update_gym(self, gym_data):
        if 'id' not in gym_data:
            raise HttpException(400, 'Could not update gym without id provided')
        raise HttpException(501, 'Not implemented')

    def delete_gym(self, gym_id):
        no_deleted_rows = self.gym_dao.delete().where(self.gym_dao.gym_id == gym_id).execute()
        return bool(no_deleted_rows)