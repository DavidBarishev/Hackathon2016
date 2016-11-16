from pycnic.core import WSGI, Handler
from waitress import serve


class TicketService(Handler):

    def get(self,id,name):
        return {
            name:id
        }

class TrainService(Handler):

    def get(self,id):
        return {
            'trainID':id
        }

class RootService(Handler):

    def get(self):
        return {
            "root":''
        }


class app(WSGI):
    routes = [
        ('/tickets/([\d]{9})/([\w]+)', TicketService()),
        ('/trains/([\d]+)', TrainService()),
        ('/',RootService())

    ]

serve(app, listen='*:8080')
