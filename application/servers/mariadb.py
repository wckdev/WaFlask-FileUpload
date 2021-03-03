class MariaDB(object):

	def __init__(self):
		self.configuration = {
			'host':         '127.0.0.1',
			'port':         3306,
			'database':     'test',
			'user':         'alumno',
			'password':     '123456789',
			'charset':      'utf8',
			'use_unicode':  True,
			'get_warnings': True,
		}
