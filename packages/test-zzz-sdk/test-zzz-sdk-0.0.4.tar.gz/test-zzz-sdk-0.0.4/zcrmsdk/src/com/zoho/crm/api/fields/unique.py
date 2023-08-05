from ..util import Model


class Unique(Model):
	def __init__(self):
		self.__casesensitive = None
		self.__key_modified = dict()

	def get_casesensitive(self):
		return self.__casesensitive

	def set_casesensitive(self, casesensitive):
		self.__casesensitive = casesensitive
		self.__key_modified["casesensitive"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
