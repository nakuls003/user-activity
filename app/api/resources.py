from flask_restful import Resource, Api, abort
from sqlalchemy import and_
from . import api
from webargs.flaskparser import parser
from webargs import fields, ValidationError
from app.models import UserActivity
from .serializers import UserActivitySerializer
from datetime import datetime

user_activity_api = Api(api)


@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_headers):
    abort(error_status_code, errors=err.messages)


def _validate_date_range(val):
    """
    datetime validation logic goes here. Valid datetime examples are:
    2018-08-21, 2018-08-21 09:21:36 etc.
    """
    date_obj = val.split(' ')[0]
    time_obj = val.split(' ')[1] if ' ' in val else '00:00:00'
    try:
        datetime.strptime(date_obj + ' ' + time_obj, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValidationError('datetime format not accepted, please enter in yyyy-mm-dd h:m:s form')


class UserActivityResource(Resource):

    """
    API to get user activity log needed to build notification feed
    Example URL: http://localhost:5000/api/v1/feed?from=2019-01-26 12:05:27&to=2019-01-30&userid=1
    """

    get_args = {
        'from': fields.Str(required=True, location='querystring', validate=_validate_date_range),
        'to': fields.Str(required=True, location='querystring', validate=_validate_date_range),
        'userid': fields.Int()
    }

    def get(self):
        args_dict = parser.parse(self.get_args)
        from_time = args_dict.get('from')
        to_time = args_dict.get('to')
        user_id = args_dict.get('userid')
        query = UserActivity.query.filter(and_(UserActivity.timestamp >= from_time),
                                          (UserActivity.timestamp <= to_time))
        if user_id:
            query = query.filter(UserActivity.user_id == user_id)
        output = UserActivitySerializer(many=True).dump(query)
        return output


user_activity_api.add_resource(UserActivityResource, '/feed', endpoint='get_activity_feed')
