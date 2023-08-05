from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__variable_groups = None
		self.__key_modified = dict()

	def get_variable_groups(self):
		return self.__variable_groups

	def set_variable_groups(self, variable_groups):
		self.__variable_groups = variable_groups
		self.__key_modified["variable_groups"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
