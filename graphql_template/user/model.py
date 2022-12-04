from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True)
    name = fields.CharField(max_length=128)
