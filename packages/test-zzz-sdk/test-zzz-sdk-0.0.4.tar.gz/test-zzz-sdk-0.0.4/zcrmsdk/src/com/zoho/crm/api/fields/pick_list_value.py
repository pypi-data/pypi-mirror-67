from ..util import Model


class PickListValue(Model):
	def __init__(self):
		self.__display_value = None
		self.__actual_value = None
		self.__key_modified = dict()

	def get_display_value(self):
		return self.__display_value

	def set_display_value(self, display_value):
		self.__display_value = display_value
		self.__key_modified["display_value"] = 1

	def get_actual_value(self):
		return self.__actual_value

	def set_actual_value(self, actual_value):
		self.__actual_value = actual_value
		self.__key_modified["actual_value"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
