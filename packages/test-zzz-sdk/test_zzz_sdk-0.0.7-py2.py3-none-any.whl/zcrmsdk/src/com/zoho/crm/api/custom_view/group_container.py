from ..util import Model


class GroupContainer(Model):
	def __init__(self):
		self.__comparator = None
		self.__field = None
		self.__value = None
		self.__key_modified = dict()

	def get_comparator(self):
		return self.__comparator

	def set_comparator(self, comparator):
		self.__comparator = comparator
		self.__key_modified["comparator"] = 1

	def get_field(self):
		return self.__field

	def set_field(self, field):
		self.__field = field
		self.__key_modified["field"] = 1

	def get_value(self):
		return self.__value

	def set_value(self, value):
		self.__value = value
		self.__key_modified["value"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
