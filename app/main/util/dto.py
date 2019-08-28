from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'id': fields.Integer(required=True, description='user id'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user latst name'),
        'company_name': fields.String(required=True, description='user company name'),
        'city': fields.String(required=True, description='user city'),
        'state': fields.String(required=True, description='user state'),
        'zip': fields.Integer(description='user zip'),
        'email': fields.String(description='user email'),
        'web': fields.String(description='user web'),
        'age': fields.Integer(description='user age')

    })

 