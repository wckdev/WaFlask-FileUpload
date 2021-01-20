from werkzeug.security import generate_password_hash, check_password_hash

from os import getcwd
from os import listdir
from os import mkdir

from os.path import exists
from os.path import isdir

from random import randint as rnd

from datetime import datetime

def crypt(secret_key):
	return generate_password_hash(secret_key)

def decrypt(hash, secret_key):
	return check_password_hash(hash, secret_key)
