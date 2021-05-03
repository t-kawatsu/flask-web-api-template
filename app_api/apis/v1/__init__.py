from flask import Blueprint, current_app
from flask_restx import Api, fields
from .health import ns as health
from .users import ns as users

from werkzeug.exceptions import HTTPException
from urllib.error import URLError


bp = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(bp, catch_all_404s=True)


@api.errorhandler(URLError)
@api.errorhandler(HTTPException)
@api.marshal_with({
    'error': fields.Nested({
        'code': fields.String,
        'message': fields.String,
    })
})
def buisiness_exception_handler(error):
    error_code = getattr(error, 'code', None)
    status_code = error_code if isinstance(error_code, int) else 500
    status_code_map = {
        400: 'invalid_request',
        401: 'invalid_token',
        404: 'not_found',
        405: 'invalid_request',
        500: 'internal_server_error',
    }
    if status_code not in status_code_map:
        code = 'internal_server_error'
    else:
        code = status_code_map[status_code]

    return {
        'error': {
            'code': code,
            'message': str(error)
        }
    }, status_code


@api.errorhandler
def error_handler(error):
    if current_app.config.get('TESTING', False):
        raise error
    return buisiness_exception_handler(error)


api.add_namespace(health)
api.add_namespace(users)
