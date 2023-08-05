from ..util import Model


class Category(Model):
	def __init__(self):
		self.__display_label = None
		self.__permissions_details = None
		self.__name = None
		self.__key_modified = dict()

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_permissions_details(self):
		return self.__permissions_details

	def set_permissions_details(self, permissions_details):
		self.__permissions_details = permissions_details
		self.__key_modified["permissions_details"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
