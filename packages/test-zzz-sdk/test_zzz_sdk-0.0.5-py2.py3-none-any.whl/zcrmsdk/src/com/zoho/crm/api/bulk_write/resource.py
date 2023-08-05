from ..util import Model


class Resource(Model):
	def __init__(self):
		self.__type = None
		self.__module = None
		self.__file_id = None
		self.__ignore_empty = None
		self.__find_by = None
		self.__field_mappings = None
		self.__file = None
		self.__key_modified = dict()

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type
		self.__key_modified["type"] = 1

	def get_module(self):
		return self.__module

	def set_module(self, module):
		self.__module = module
		self.__key_modified["module"] = 1

	def get_file_id(self):
		return self.__file_id

	def set_file_id(self, file_id):
		self.__file_id = file_id
		self.__key_modified["file_id"] = 1

	def get_ignore_empty(self):
		return self.__ignore_empty

	def set_ignore_empty(self, ignore_empty):
		self.__ignore_empty = ignore_empty
		self.__key_modified["ignore_empty"] = 1

	def get_find_by(self):
		return self.__find_by

	def set_find_by(self, find_by):
		self.__find_by = find_by
		self.__key_modified["find_by"] = 1

	def get_field_mappings(self):
		return self.__field_mappings

	def set_field_mappings(self, field_mappings):
		self.__field_mappings = field_mappings
		self.__key_modified["field_mappings"] = 1

	def get_file(self):
		return self.__file

	def set_file(self, file):
		self.__file = file
		self.__key_modified["file"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
