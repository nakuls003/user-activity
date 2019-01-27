from marshmallow_sqlalchemy import ModelSchema
from app.models import UserActivity


class UserActivitySerializer(ModelSchema):
    class Meta:
        model = UserActivity
