from ..util import Model


class ResponseWrapper(Model):
	def __init__(self):
		self.__variables = None
		self.__key_modified = dict()

	def get_variables(self):
		return self.__variables

	def set_variables(self, variables):
		self.__variables = variables
		self.__key_modified["variables"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
