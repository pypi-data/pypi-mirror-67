from ..fields import ToolTip
from ..util import Model


class Properties(Model):
	def __init__(self):
		self.__reorder_rows = None
		self.__tooltip = None
		self.__maximum_rows = None
		self.__key_modified = dict()

	def get_reorder_rows(self):
		return self.__reorder_rows

	def set_reorder_rows(self, reorder_rows):
		self.__reorder_rows = reorder_rows
		self.__key_modified["reorder_rows"] = 1

	def get_tooltip(self):
		return self.__tooltip

	def set_tooltip(self, tooltip):
		self.__tooltip = tooltip
		self.__key_modified["tooltip"] = 1

	def get_maximum_rows(self):
		return self.__maximum_rows

	def set_maximum_rows(self, maximum_rows):
		self.__maximum_rows = maximum_rows
		self.__key_modified["maximum_rows"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
