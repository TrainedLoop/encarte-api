from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'name': fields.String(required=True,description='user name'),
        'document': fields.String(required=True, description='user document'),
        'admin': fields.Boolean(description='user admin status')
    })
    userEdit = api.model('userEdit', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(description='user password'),

        'public_id': fields.String(required=True,description='user Identifier'),
        'name': fields.String(required=True,description='user name'),
        'document': fields.String(required=True,description='user document'),
        'admin': fields.Boolean(description='user admin status')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


    
class EncarteDTO:
    api = Namespace('encarte', description='encarte related operations')
    encarte = api.model('create_encarte', {
        #'image': fields.String(required=True),
        'user_id': fields.String(required=True),
        'id': fields.Integer(required=True),
        'uploaded_by': fields.String(required=True),
        'create_date': fields.Date(required=True),
        'start_date': fields.Date(required=True),
        'end_date': fields.Date(required=True),
        'brand_id': fields.String(required=True),
        'state': fields.String(required=True),



        })

    create_encarte = api.model('create_encarte', {
        'image': fields.String(required=True),
        'user_id': fields.String(required=True),
        'start_date': fields.Date(required=True),
        'end_date': fields.Date(required=True),
        'brand_id': fields.Date(required=True),
    })

