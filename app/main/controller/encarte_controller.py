from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import EncarteDTO
from ..service.encarte_service import save_new_encarte, get_encartes
from app.main.service.auth_helper import Auth

api = EncarteDTO.api
_create_encarte = EncarteDTO.create_encarte
_encarte = EncarteDTO.encarte



@api.route('/')
class Encarte(Resource):
    @api.expect(_create_encarte, validate=True)
    @api.doc('create encarte')
    @api.response(201, 'Encarte successfully created.')
    def post(self):
        data = request.json
        return save_new_encarte(data=data)

    @api.doc('list_of_registered_encartes')
    @api.marshal_list_with(_encarte, envelope='data')

    def get(self):
        print(request.args)
        return get_encartes()
