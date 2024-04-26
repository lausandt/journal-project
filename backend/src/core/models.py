from enum import Enum

from tortoise.fields import (
    CharEnumField,
    CharField,
    DatetimeField,
    ForeignKeyField,
    ForeignKeyRelation,
    IntField,
    TextField,
)
from tortoise.models import Model


class Period(str, Enum):
    weekly: str = 'Weekly'
    fourweekly: str = 'Four weekly'
    monthly: str = 'Montly'
    quarterly: str = 'Quarterly'
    yearly: str = 'Yearly'


class User(Model):
    id: IntField = IntField(pk=True)
    name: CharField = CharField(max_length=64)
    email: CharField = CharField(max_length=128, unique=True)
    password: CharField = CharField(max_length=128)
    creadate: DatetimeField = DatetimeField(auto_now_add=True, null=True)
    modate: DatetimeField = DatetimeField(auto_now=True, null=True)

    def __repr__(self) -> str:
        return f'Class [{self.__class__.__name__} id: {self.id} email: {self.email} creation date: {self.creadate}]'


class Entry(Model):
    id: IntField = IntField(pk=True)
    name: CharField = CharField(max_length=64)
    description: TextField = TextField()
    author: ForeignKeyRelation[User] = ForeignKeyField('models.User', related_name='entry')
    creadate: DatetimeField = DatetimeField(auto_now_add=True, null=True)
    modate: DatetimeField = DatetimeField(auto_now=True, null=True)

    def __repr__(self) -> str:
        return f'Class [{self.__class__.__name__} id: {self.id} author: {self.author_id} creation date: {self.creadate}]'


class RegularEntry(Entry):
    author: ForeignKeyRelation[User] = ForeignKeyField('models.User', related_name='regular entry')
    period: CharEnumField = CharEnumField(enum_type=Period)

    def __repr__(self) -> str:
        return f'Class [{self.__class__.__name__} id: {self.id} author: {self.author_id} creation date: {self.creadate}]'
