from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__related_lists = None
		self.__key_modified = dict()

	def get_related_lists(self):
		return self.__related_lists

	def set_related_lists(self, related_lists):
		self.__related_lists = related_lists
		self.__key_modified["related_lists"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
