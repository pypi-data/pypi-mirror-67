from ..util import Model


class Currency(Model):
	def __init__(self):
		self.__rounding_option = None
		self.__precision = None
		self.__key_modified = dict()

	def get_rounding_option(self):
		return self.__rounding_option

	def set_rounding_option(self, rounding_option):
		self.__rounding_option = rounding_option
		self.__key_modified["rounding_option"] = 1

	def get_precision(self):
		return self.__precision

	def set_precision(self, precision):
		self.__precision = precision
		self.__key_modified["precision"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
