from peewee import *

from core.DBPool import DBPool
from core.Config import Config


class BaseModel(Model):
    class Meta:
        database = None


class Items(BaseModel):

    barcode = CharField()
    homebranch = CharField()



