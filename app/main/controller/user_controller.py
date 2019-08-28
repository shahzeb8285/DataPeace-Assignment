from flask import request
from flask_restplus import Resource


from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, delete_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user)
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
class User(Resource):
    @api.doc('get a user')
    @api.response(404, 'User not found.')

    @api.marshal_with(_user)
    def get(self, id):
        """get a user given its identifier"""
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
            return user
    @api.doc('delete a user')
    @api.marshal_with(_user)
    def delete(self, id):
        print(id)
        delete_a_user(id)
        return {}




