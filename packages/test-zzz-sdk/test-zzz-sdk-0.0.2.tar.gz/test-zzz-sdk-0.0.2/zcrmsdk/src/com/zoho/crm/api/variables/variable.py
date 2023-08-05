from ..util import Model
from ..variablegroups import VariableGroup


class Variable(Model):
	def __init__(self):
		self.__id = None
		self.__api_name = None
		self.__name = None
		self.__description = None
		self.__type = None
		self.__value = None
		self.__variable_group = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description
		self.__key_modified["description"] = 1

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type
		self.__key_modified["type"] = 1

	def get_value(self):
		return self.__value

	def set_value(self, value):
		self.__value = value
		self.__key_modified["value"] = 1

	def get_variable_group(self):
		return self.__variable_group

	def set_variable_group(self, variable_group):
		self.__variable_group = variable_group
		self.__key_modified["variable_group"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
