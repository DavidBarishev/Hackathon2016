# from Backend.py

from waitress import serve
from pycnic.core import WSGI, Handler
from pycnic.errors import HTTP_400
from DBFunctions import *
import time

db = Database("database.db")

class Echo(Handler):
    def get(self):
        return{
            'working': True
        }


class User_Login(Handler):
    def post(self):
        user_id = self.request.data.get("user_id")
        password = self.request.data.get("password")
        return{
        db.check_credentials(user_id, password, "student")
        }


class Start_Vol(Handler):
    def post(self):
        startf = open('start_end_vol', 'r+')
        startf.write(time.strftime("%X"))
        startf.close()


class End_Vol(Handler):
    def post(self):
        startf = open('start_end_vol', 'r+')
        start_time = startf.read(5).split(':')
        end_time = time.strftime("%X").split(':')
        time_volunteered = (int(end_time[0] * 60 + end_time[1])) - (int(start_time[0] * 60 + start_time[1]))
        db.add_mins_done(time_volunteered)
        startf.close()


class Add_Student(Handler):
    def post(self):
        if not self.request.data.get("first_name", "last_name", "grade"):
            raise HTTP_400("Please fill in all the required fields.")
        else:
            data = self.request.data
            db.add_student(data["first_name"], data["last_name"], data["grade"])


class Get_Status(Handler):
    def get(self, user_id):
        hours_per_month = db.get_mins_done(user_id) / int(time.strftime("%x").split("/")[0])
        return {
            'hours_done': db.get_mins_done(user_id),
            'hours_per_month': hours_per_month
        }

class app(WSGI):
    routes = [
        ("/", Echo()),
        ("/user_id/211658471", Get_Status()),
        ("/start_vol", Start_Vol()),
        ("/end_vol", End_Vol()),
        ("/add_student", Add_Student())
        ]

if __name__ == '__main__':
    serve(app, listen="localhost:8080")
    db.close()