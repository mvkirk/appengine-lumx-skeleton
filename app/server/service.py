import webapp2
from server import jsonEncode


class Service(webapp2.RequestHandler):

    def get(self):
        response = {
            'message': 'Hello World'
        }
        self.response.write(jsonEncode.encode(response))

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass