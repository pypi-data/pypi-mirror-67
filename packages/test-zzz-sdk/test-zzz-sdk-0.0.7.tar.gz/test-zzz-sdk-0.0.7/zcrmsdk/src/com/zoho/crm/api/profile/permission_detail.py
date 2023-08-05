from ..util import Model


class PermissionDetail(Model):
	def __init__(self):
		self.__display_label = None
		self.__module = None
		self.__name = None
		self.__id = None
		self.__enabled = None
		self.__key_modified = dict()

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_module(self):
		return self.__module

	def set_module(self, module):
		self.__module = module
		self.__key_modified["module"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_enabled(self):
		return self.__enabled

	def set_enabled(self, enabled):
		self.__enabled = enabled
		self.__key_modified["enabled"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
