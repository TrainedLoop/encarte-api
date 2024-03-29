from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.encarte_controller import api as encarte_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='ENCARTE API',
          version='1.0',
          description='Encarte API web service')

api.add_namespace(user_ns, path='/user')
api.add_namespace(encarte_ns, path='/encarte')
api.add_namespace(auth_ns)