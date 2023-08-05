from ..util import Model

from .response_handler import ResponseHandler

class ResponseWrapper(Model, ResponseHandler):
	def __init__(self):
		self.__org = None
		self.__key_modified = dict()

	def get_org(self):
		return self.__org

	def set_org(self, org):
		self.__org = org
		self.__key_modified["org"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
