from common.exceptions import ValidationError

from flask_restful import Resource


class UserResource(Resource):
    def get(self):
        # return {'hello': 'world'}
        raise ValidationError('dfs')
