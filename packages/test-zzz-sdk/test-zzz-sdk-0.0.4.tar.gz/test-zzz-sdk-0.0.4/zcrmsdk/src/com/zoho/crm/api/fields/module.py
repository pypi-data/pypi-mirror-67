from ..util import Model


class Module(Model):
	def __init__(self):
		self.__display_label = None
		self.__api_name = None
		self.__module = None
		self.__id = None
		self.__key_modified = dict()

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_module(self):
		return self.__module

	def set_module(self, module):
		self.__module = module
		self.__key_modified["module"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
