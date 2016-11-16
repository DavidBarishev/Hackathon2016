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
			self.create_db()

	def create_db(self):
		""" Creates a new database. """
		self._db.executescript("""
			CREATE TABLE 'Users'
			(
				'UserCode'		INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
				'Password'		TEXT,
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
				'CompanyID'		BIGINT REFERENCES 'Companies' ('CompanyID')
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


	def _add_user(self, password, permission):
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


	def add_student(self, student_id, password, firstname, lastname, grade, company_id=None):
		"""
		Adds the student and its info to the database.
		:params: Student info.
		"""
		usercode = self._add_user(password, 'student')
		self._db.execute("""
			INSERT INTO Students (UserCode, StudentID, FirstName, LastName, Grade, CompanyID)
			VALUES (%d, %d, '%s', '%s', %d, %d)
		""" % (usercode, student_id, firstname, lastname, grade, company_id))
		self._conn.commit()


	def add_company(self, company_id, password, name):
		"""
		Adds the company and its info to the database.
		:params: The company's info.
		"""
		usercode = self._add_user(password, 'company')
		self._db.execute("""
			INSERT INTO Companies (UserCode, CompanyID, Name)
			VALUES (%d, %d, '%s')
		""" % (usercode, company_id, name))
		self._conn.commit()


	def get_mins_done(self, student_id):
		"""
		This function returns the amount of minutes student has done.
		:param student_id: (INT) Student's ID.
		:return : (INT) Amount of minutes student has done.
		"""
		self._db.execute("""
			SELECT MinsDone
			FROM Students
			WHERE StudentID = %d
		""" % student_id)
		return self._db.fetchone()[0]


	def add_mins_done(self, student_id, mins):
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


	def get_volunteers_of_company(self, company_id):
		"""
		This function returns all the students that volunteer at a given company.
		:param company_id: (INT) Company's ID
		:return: A list of tuples containing the Student's ID and name. (ID, first name, last name)
		"""
		self._db.execute("""
			SELECT StudentID, FirstName, LastName
			FROM Students
			WHERE CompanyID = %d
		""" % company_id)
		return self._db.fetchall()


	def check_credentials(self, user_id, password, permission):
		"""
		Check if the StudentID or CompanyID and password are correct.
		:param user_id: StudentID or CompanyID.
		:param password: User's password.
		:param permission: The user's permission.
		:return: Return True/False - if the ID and Password are correct.
		"""
		# check if the student's ID is valid
		if permission == "student":
			self._db.execute("""
				SELECT UserCode
				FROM Students
				WHERE StudentID = %d
			""" % user_id)

		# check if the company's ID is valid
		elif permission == "company":
			self._db.execute("""
				SELECT UserCode
				FROM Companies
				WHERE CompanyID = %d
			""" % user_id)

		temp = self._db.fetchone()
		usercode = temp[0] if temp else False
		if usercode:
			self._db.execute("""
				SELECT UserCode
				FROM Users
				WHERE UserCode = %d AND Password = '%s'
			""" % (usercode, password))
			if self._db.fetchone(): return True

		return False


	def get_student_info(self, student_id):
		self._db.execute("""
			SELECT FirstName, LastName, Grade, MinsDone, CompanyID
			FROM Students
			WHERE StudentID = %d
		""" % student_id)
		return self._db.fetchone()


	def get_company_info(self, company_id):
		self._db.execute("""
			SELECT Name
			FROM Companies
			WHERE CompanyID = %d
		""" % company_id)
		return self._db.fetchone()
