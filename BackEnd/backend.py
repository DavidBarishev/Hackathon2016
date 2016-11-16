from pycnic.core import WSGI, Handler
from waitress import serve
from DBFunctions import *
import time

class OnlineService(Handler):
    def get(self):
        return {
            'succsess':True
        }


class GetUserStatuesService(Handler):
    def get(self,id):
        id = int(id)
        db = Database('database.db')
        mins_done = db.get_mins_done(id)
        v = int(time.strftime("%x").split("/")[0])
        mins_per_month =  mins_done/v
        info = db.get_student_info(id)
        if info[2] == 11 or info[2] == 10:
            minutes_left = 3600-mins_done 
        elif info[2] == 12:
            minutes_left = 1800-mins_done
        companyId = info[4]
        companyName = None
        if companyId is not None:
            companyName = db.get_company_info(company_id)[0]
        db.close() 
        return {
            'companyName': companyName if companyName else '',
            'first_name': info[0],
            'last_name': info[1],
            'mins_done': mins_done,
            'minutes_per_month': mins_per_month,
            'minutes_left': minutes_left
        }

class User_Login(Handler):
    def post(self):
        db = Database('database.db')
        user_id = self.request.data.get("user_id")
        password = self.request.data.get("password")
        isGood = db.check_credentials(user_id, password, "student")
        db.close()
        return{
        'login': isGood
        }


class start_vol(Handler):
    def post(self):
        id = str(self.request.data.get("user_id"))
        timestamp = time.strftime("%X")
        currentlyActive[id] = timestamp
        return {
                'success':True
        }

class End_Vol(Handler):
    def post(self):
        id = str(self.request.data.get("user_id"))

        try:
            start_time = currentlyActive[id].split(':')
            end_time = time.strftime("%X").split(':')
            time_volunteered = (int(end_time[0]) * 60 + int(end_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))
               
            db = Database('database.db')
            db.add_mins_done(int(id),time_volunteered)
            db.close()

            return {
                'success':True
            }

        except KeyError:
            raise HTTP_400('User isnt active')
               
        
        


class Add_Student(Handler):
    def post(self):
        db = Database('database.db')
        data = self.request.data
        db.add_student(int(data['id']),data['password'],data["first_name"], data["last_name"], data["grade"])
        db.close()
        return {
            'success':True
        }

class app(WSGI):
    routes = [
        ('/',OnlineService()),
        ('/api/user_status/([\d]{9})',GetUserStatuesService()),
        ('/api/login',User_Login()),
        ('/api/start_vol',start_vol()),
        ('/api/end_vol',End_Vol()),
        ('/api/add',Add_Student()),

    ]
def main():
    global currentlyActive
    currentlyActive = {}
    serve(app, listen='*:8080')

if __name__ == '__main__':
    main()

