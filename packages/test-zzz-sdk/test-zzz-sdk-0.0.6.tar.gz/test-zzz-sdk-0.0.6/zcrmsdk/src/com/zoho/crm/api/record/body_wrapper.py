from ..util import Model


class BodyWrapper(Model):
	def __init__(self):
		self.__data = None
		self.__trigger = None
		self.__lar_id = None
		self.__key_modified = dict()

	def get_data(self):
		return self.__data

	def set_data(self, data):
		self.__data = data
		self.__key_modified["data"] = 1

	def get_trigger(self):
		return self.__trigger

	def set_trigger(self, trigger):
		self.__trigger = trigger
		self.__key_modified["trigger"] = 1

	def get_lar_id(self):
		return self.__lar_id

	def set_lar_id(self, lar_id):
		self.__lar_id = lar_id
		self.__key_modified["lar_id"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
