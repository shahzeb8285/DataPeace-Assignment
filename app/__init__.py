from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CloudPeace Users API',
          version='1.0',
          description='create get and delete users'
          )

api.add_namespace(user_ns, path='/api/users')
