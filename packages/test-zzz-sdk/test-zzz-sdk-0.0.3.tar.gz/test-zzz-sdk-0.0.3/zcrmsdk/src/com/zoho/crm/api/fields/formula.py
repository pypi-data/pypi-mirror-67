from ..util import Model


class Formula(Model):
	def __init__(self):
		self.__return_type = None
		self.__key_modified = dict()

	def get_return_type(self):
		return self.__return_type

	def set_return_type(self, return_type):
		self.__return_type = return_type
		self.__key_modified["return_type"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
