from common.exceptions import HttpException
from dao import Booking
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict, dict_to_model

class BookingService():
    def __init__(self):
        self.booking_dao = None

    def get_all_bookings(self):
        bookings_list = self.booking_dao.select()
        return [model_to_dict(u) for u in bookings_list]
    
    def get_by_id(self, booking_id):
        try:
            return model_to_dict(self.booking_dao.get(self.booking_dao.booking_id == booking_id))
        except DoesNotExist:
            return None

    def create_gym(self, booking_data):
        #TODO
        raise HttpException(501, 'Not implemented')
    
    def update_gym(self, booking_data):
        if 'id' not in booking_data:
            raise HttpException(400, 'Could not update booking without id provided')
        raise HttpException(501, 'Not implemented')

    def delete_gym(self, booking_id):
        no_deleted_rows = self.booking_dao.delete().where(self.booking_dao.booking_id == booking_id).execute()
        return bool(no_deleted_rows)