from flask import request, session
from flask_restplus import Resource

from ..service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
    User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data {'email': '....', 'password': '...'}
        post_data = request.json
        # FJE - add auth-token to session, original using header
        response = Auth.login_user(data=post_data)
        session['Authorization'] = response[0].get('Authorization')
        return response  # Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token - headers didn't work
        # auth_header = request.headers.get('Authorization')
        # FJE - does work with session
        print('debug headers:', request.headers.get('Authorization'))
        auth_header = session['Authorization']
        return Auth.logout_user(data=auth_header)
