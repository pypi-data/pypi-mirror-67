from ..util import Model

from .count_handler import CountHandler

class CountWrapper(Model, CountHandler):
	def __init__(self):
		self.__count = None
		self.__key_modified = dict()

	def get_count(self):
		return self.__count

	def set_count(self, count):
		self.__count = count
		self.__key_modified["count"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
