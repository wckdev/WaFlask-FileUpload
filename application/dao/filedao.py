import mysql.connector
import sqlite3

from ..servers.mariadb import MariaDB
from ..helpers.helper import crypt
from ..helpers.helper import decrypt

class FileDAO(MariaDB):

	def __init__(self, db):
		MariaDB.__init__(self)
		self.__db = db

	def uploadFile(self, data):
		try:
			link = mysql.connector.Connect(**self.configuration)
			cursor = link.cursor()
			response = cursor.execute("INSERT INTO files VALUES(null, '{}', '{}', '{}', NOW())".format(data[0], data[1], data[2]))

			if cursor.rowcount > 0:
				return True
			else:
				return False

		except mysql.connector.Error as error:
			print(error)
		finally:
			if link.is_connected():
				link.commit()
				cursor.close()
				link.close()
