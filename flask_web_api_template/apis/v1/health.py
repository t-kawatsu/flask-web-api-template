from flask_restx import Namespace, Resource

ns = Namespace('health')


@ns.route('')
class Health(Resource):
    def get(self):
        return {'status': 'fine'}
