from ..record import Record
from ..util import Model


class FieldMapping(Model):
	def __init__(self):
		self.__api_name = None
		self.__index = None
		self.__format = None
		self.__find_by = None
		self.__default_value = None
		self.__key_modified = dict()

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_index(self):
		return self.__index

	def set_index(self, index):
		self.__index = index
		self.__key_modified["index"] = 1

	def get_format(self):
		return self.__format

	def set_format(self, format):
		self.__format = format
		self.__key_modified["format"] = 1

	def get_find_by(self):
		return self.__find_by

	def set_find_by(self, find_by):
		self.__find_by = find_by
		self.__key_modified["find_by"] = 1

	def get_default_value(self):
		return self.__default_value

	def set_default_value(self, default_value):
		self.__default_value = default_value
		self.__key_modified["default_value"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
