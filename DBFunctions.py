import os.path
import sqlite3


class Database:
	_path = None
	_conn = None
	_db = None

	def __init__(self, file_name):
		self._path = file_name
		create = not os.path.isfile(self._path)
		self._conn = sqlite3.connect(self._path)   # connect to the database
		self._db = self._conn.cursor()
		if create:
			self.createDB()

	def createDB(self):
		""" Creates a new database. """
		self._db.executescript("""
			CREATE TABLE 'Users'
			(
				'UserCode'		INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
				'Password'		TEXT
				'Permission'	TEXT
			);

			CREATE TABLE 'Students'
			(
				'UserCode'		INT PRIMARY KEY REFERENCES 'Users' ('UserCode'),
				'StudentID' 	INT,
				'FirstName'		TEXT,
				'LastName'		TEXT,
				'Grade'			TINYINT,
				'MinsDone'		INT DEFAULT 0,
				'CompanyID'		BIGINT DEFAULT NULL REFERENCES 'Companies' ('CompanyID')
			);

			CREATE TABLE 'Companies'
			(
				'UserCode'		INT PRIMARY KEY REFERENCES 'Users' ('UserCode'),
				'CompanyID'		BIGINT,
				'Name'			TEXT
			);
		""")
		self._conn.commit()


	def close(self):
		""" Closes the connection to the database. """
		self._conn.close()


	def _addUser(self, password, permission):
		"""
		Adds a user to the 'Users' table and returns its user code.
		:return: The new user's code.
		"""
		self._db.execute("""
			INSERT INTO Users (Password, Permission)
			VALUES ('%s', '%s')
		""" % (password, permission))
		self._conn.commit()
		self._db.execute("""
			SELECT UserCode
			FROM Users
			ORDER BY UserCode DESC
			LIMIT 1
		""")
		return self._db.fetchone()[0]


	def addStudent(self, student_id, password, firstname, lastname, grade):
		"""
		Adds the student and its info to the database.
		:params: Student info.
		"""
		usercode = self._addUser(password, 'student')
		self._db.execute("""
			INSERT INTO Students (UserCode, StudentID, FirstName, LastName, Grade)
			VALUES (%d, %d, '%s', '%s', %d)
		""" % (usercode, student_id, firstname, lastname, grade))
		self._conn.commit()


	def addCompany(self, company_id, password, name):
		"""
		Adds the company and its info to the database.
		:params: The company's info.
		"""
		usercode = self._addUser(password, 'company')
		self._db.execute("""
			INSERT INTO Companies (UserCode, CompanyID, Name)
			VALUES (%d, %d, '%s')
		""" % (usercode, company_id, name))
		self._conn.commit()


	def minsDone(self, student_id):
		"""
		This function returns the amount of minutes student has done.
		:param student_id: (INT) Student's ID.
		:return : (INT) Amount of minutes student has done.
		"""
		return self._db.execute("""
			SELECT MinsDone
			FROM Students
			WHERE StudentID = %d
		""" % student_id)


	def addMins(self, student_id, mins):
		"""
		This function adds minutes to the student's minutes done.
		:param student_id: (INT) Student's ID.
		:param mins: (INT) Amount of minutes to add.
		"""
		self._db.execute("""
			UPDATE Students
			SET MinsDone = MinsDone + %d
			WHERE StudentID = %d
		""" % (mins, student_id))
		self._conn.commit()


