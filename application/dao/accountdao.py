import mysql.connector
import sqlite3

from ..servers.mariadb import MariaDB
from ..helpers.helper import crypt
from ..helpers.helper import decrypt

class AccountDAO(MariaDB):

	def __init__(self, db):
		MariaDB.__init__(self)
		self.__db = db

	# MariaDB - Login

	
	def addAdmin(self, nickname, secret_key):
		#secret_key = crypt(secret_key)
		pass

	def login(self, nickname, secret_key):
		try:
			link = mysql.connector.Connect(**self.configuration)
			cursor = link.cursor()
			cursor.execute("SELECT secret_key FROM accounts WHERE nickname = '{}'".format(nickname))
			data = cursor.fetchone()

			if data is None:
				return False
			else:
				hash = data[0]
				hash = ''.join(str(e) for e in hash.decode('utf-8'))
				if decrypt(hash, secret_key):

					link = mysql.connector.Connect(**self.configuration)
					cursor = link.cursor()
					cursor.execute("UPDATE accounts SET secret_key = '{}' WHERE nickname = '{}'".format(crypt(secret_key), nickname))
					link.commit()

					return True
				else:
					return False

		except mysql.connector.Error as error:
			print(error)
		finally:
			if link.is_connected():
				cursor.close()
				link.close()
	

	# SQLite3 - Login
'''
	def addAdmin(self, nickname, secret_key):
		#secret_key = crypt(secret_key)
		pass

	def login(self, nickname, secret_key):
		try:
			link = sqlite3.connect(self.__db)
			cursor = link.cursor()
			cursor.execute("SELECT secret_key FROM accounts WHERE nickname = '{}'".format(nickname))
			data = cursor.fetchone()

			if data is None:	
				return False
			else:
				hash = data[0]
				if decrypt(hash, secret_key):

					link = sqlite3.connect(self.__db)
					cursor = link.cursor()
					cursor.execute("UPDATE accounts SET secret_key = '{}' WHERE nickname = '{}'".format(crypt(secret_key), nickname))
					link.commit()

					return True
				else:
					return False

		except sqlite3.Error as e:
	 		print('An error has ocurred: ', e.args[0])
		finally:
			cursor.close()
			link.close()
'''