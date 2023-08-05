from ..util import Model


class Section(Model):
	def __init__(self):
		self.__name = None
		self.__categories = None
		self.__key_modified = dict()

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_categories(self):
		return self.__categories

	def set_categories(self, categories):
		self.__categories = categories
		self.__key_modified["categories"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
