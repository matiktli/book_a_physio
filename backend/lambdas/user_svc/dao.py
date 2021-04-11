from peewee import *
import datetime
import os

from dotenv import load_dotenv

load_dotenv()
DATABASE = MySQLDatabase('book_a_physio', host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'))

class BaseModel(Model):
    class Meta:
        database = DATABASE

class User(BaseModel):
    user_id = AutoField()
    email = CharField(unique=True, max_length=30)
    password = CharField(max_length=30)
    #[ADD_LATER] username = CharField(max_length=20)
    #[ADD_LATER] create_date = DateTimeField(default=datetime.datetime.now)

DATABASE.connect()
DATABASE.create_tables([User])