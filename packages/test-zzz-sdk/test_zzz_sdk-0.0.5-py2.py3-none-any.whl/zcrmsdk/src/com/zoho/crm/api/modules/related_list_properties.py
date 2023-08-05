from ..util import Model


class RelatedListProperties(Model):
	def __init__(self):
		self.__sort_by = None
		self.__fields = None
		self.__sort_order = None
		self.__key_modified = dict()

	def get_sort_by(self):
		return self.__sort_by

	def set_sort_by(self, sort_by):
		self.__sort_by = sort_by
		self.__key_modified["sort_by"] = 1

	def get_fields(self):
		return self.__fields

	def set_fields(self, fields):
		self.__fields = fields
		self.__key_modified["fields"] = 1

	def get_sort_order(self):
		return self.__sort_order

	def set_sort_order(self, sort_order):
		self.__sort_order = sort_order
		self.__key_modified["sort_order"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
