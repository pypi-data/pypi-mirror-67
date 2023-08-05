from ..util import Model


class BodyWrapper(Model):
	def __init__(self):
		self.__custom_views = None
		self.__key_modified = dict()

	def get_custom_views(self):
		return self.__custom_views

	def set_custom_views(self, custom_views):
		self.__custom_views = custom_views
		self.__key_modified["custom_views"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
