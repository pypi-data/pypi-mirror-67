from ..util import Model


class ToolTip(Model):
	def __init__(self):
		self.__name = None
		self.__value = None
		self.__key_modified = dict()

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_value(self):
		return self.__value

	def set_value(self, value):
		self.__value = value
		self.__key_modified["value"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
