from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__layouts = None
		self.__key_modified = dict()

	def get_layouts(self):
		return self.__layouts

	def set_layouts(self, layouts):
		self.__layouts = layouts
		self.__key_modified["layouts"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
