from uuid import uuid4

def uuidgen():
	"""
	genrate new UUID for resource id field in database
	"""
	return uuid4().hex
