from ..util import Model


class RequestWrapper(Model):
	def __init__(self):
		self.__character_encoding = None
		self.__operation = None
		self.__callback = None
		self.__resource = None
		self.__key_modified = dict()

	def get_character_encoding(self):
		return self.__character_encoding

	def set_character_encoding(self, character_encoding):
		self.__character_encoding = character_encoding
		self.__key_modified["character_encoding"] = 1

	def get_operation(self):
		return self.__operation

	def set_operation(self, operation):
		self.__operation = operation
		self.__key_modified["operation"] = 1

	def get_callback(self):
		return self.__callback

	def set_callback(self, callback):
		self.__callback = callback
		self.__key_modified["callback"] = 1

	def get_resource(self):
		return self.__resource

	def set_resource(self, resource):
		self.__resource = resource
		self.__key_modified["resource"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
