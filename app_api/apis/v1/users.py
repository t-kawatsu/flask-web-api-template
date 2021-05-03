from flask_restx import Namespace, Resource

ns = Namespace('users')


@ns.route('/')
class UserList(Resource):
    def get(self):
        return [
            {
              'id': 1,
              'name': 'hoge fuga',
            },
        ]

    def post(self):
        pass


@ns.route('/<int:id>')
class User(Resource):
    def get(self, id):
        return {
            'id': id,
            'name': 'hoge fuga',
        }

    def delete(self, id):
        pass

    def put(self, id):
        pass
