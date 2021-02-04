from werkzeug.security import generate_password_hash, check_password_hash

def crypt(secret_key):
	return generate_password_hash(secret_key)

def decrypt(hash, secret_key):
	return check_password_hash(hash, secret_key)
