from ..util import Model


class AutoNumber(Model):
	def __init__(self):
		self.__prefix = None
		self.__suffix = None
		self.__start_number = None
		self.__key_modified = dict()

	def get_prefix(self):
		return self.__prefix

	def set_prefix(self, prefix):
		self.__prefix = prefix
		self.__key_modified["prefix"] = 1

	def get_suffix(self):
		return self.__suffix

	def set_suffix(self, suffix):
		self.__suffix = suffix
		self.__key_modified["suffix"] = 1

	def get_start_number(self):
		return self.__start_number

	def set_start_number(self, start_number):
		self.__start_number = start_number
		self.__key_modified["start_number"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
