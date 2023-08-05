from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__profiles = None
		self.__key_modified = dict()

	def get_profiles(self):
		return self.__profiles

	def set_profiles(self, profiles):
		self.__profiles = profiles
		self.__key_modified["profiles"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
