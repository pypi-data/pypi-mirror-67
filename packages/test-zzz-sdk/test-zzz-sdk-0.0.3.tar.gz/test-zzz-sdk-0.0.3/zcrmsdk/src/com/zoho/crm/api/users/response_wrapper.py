from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__users = None
		self.__key_modified = dict()

	def get_users(self):
		return self.__users

	def set_users(self, users):
		self.__users = users
		self.__key_modified["users"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
