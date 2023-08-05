from ..users import User
from ..util import Model


class JobDetail(Model):
	def __init__(self):
		self.__id = None
		self.__operation = None
		self.__state = None
		self.__query = None
		self.__created_by = None
		self.__created_time = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_operation(self):
		return self.__operation

	def set_operation(self, operation):
		self.__operation = operation
		self.__key_modified["operation"] = 1

	def get_state(self):
		return self.__state

	def set_state(self, state):
		self.__state = state
		self.__key_modified["state"] = 1

	def get_query(self):
		return self.__query

	def set_query(self, query):
		self.__query = query
		self.__key_modified["query"] = 1

	def get_created_by(self):
		return self.__created_by

	def set_created_by(self, created_by):
		self.__created_by = created_by
		self.__key_modified["created_by"] = 1

	def get_created_time(self):
		return self.__created_time

	def set_created_time(self, created_time):
		self.__created_time = created_time
		self.__key_modified["created_time"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
