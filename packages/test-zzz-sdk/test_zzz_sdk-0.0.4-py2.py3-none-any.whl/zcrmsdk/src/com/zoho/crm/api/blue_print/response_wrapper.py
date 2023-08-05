from ..util import Model


class ResponseWrapper(Model):
	def __init__(self):
		self.__blueprint = None
		self.__key_modified = dict()

	def get_blueprint(self):
		return self.__blueprint

	def set_blueprint(self, blueprint):
		self.__blueprint = blueprint
		self.__key_modified["blueprint"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
