from peewee import *
import datetime
import os

from dotenv import load_dotenv

load_dotenv()
DATABASE = MySQLDatabase('book_a_physio', host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'))

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Booking(BaseModel):
    booking_id = AutoField()
    #TODO
    gym_id = IntegerField(unique=True)
    user_id = IntegerField(unique=True)

DATABASE.connect()
DATABASE.create_tables([Booking])