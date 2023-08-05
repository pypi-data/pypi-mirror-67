from ..users import User
from ..util import Model


class Tag(Model):
	def __init__(self):
		self.__id = None
		self.__name = None
		self.__created_time = None
		self.__modified_time = None
		self.__created_by = None
		self.__modified_by = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_created_time(self):
		return self.__created_time

	def set_created_time(self, created_time):
		self.__created_time = created_time
		self.__key_modified["created_time"] = 1

	def get_modified_time(self):
		return self.__modified_time

	def set_modified_time(self, modified_time):
		self.__modified_time = modified_time
		self.__key_modified["modified_time"] = 1

	def get_created_by(self):
		return self.__created_by

	def set_created_by(self, created_by):
		self.__created_by = created_by
		self.__key_modified["created_by"] = 1

	def get_modified_by(self):
		return self.__modified_by

	def set_modified_by(self, modified_by):
		self.__modified_by = modified_by
		self.__key_modified["modified_by"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
