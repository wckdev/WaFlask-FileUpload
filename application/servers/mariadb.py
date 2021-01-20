class MariaDB(object):

	def __init__(self):
		self.configuration = {
			'host':         '127.0.0.1',
			'port':         3306,
			'database':     'test',
			'user':         'wacko',
			'password':     'wacko',
			'charset':      'utf8',
			'use_unicode':  True,
			'get_warnings': True,
		}
