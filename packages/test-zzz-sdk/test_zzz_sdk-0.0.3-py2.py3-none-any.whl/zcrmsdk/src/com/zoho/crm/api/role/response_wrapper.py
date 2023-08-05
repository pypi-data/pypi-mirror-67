from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__roles = None
		self.__key_modified = dict()

	def get_roles(self):
		return self.__roles

	def set_roles(self, roles):
		self.__roles = roles
		self.__key_modified["roles"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
