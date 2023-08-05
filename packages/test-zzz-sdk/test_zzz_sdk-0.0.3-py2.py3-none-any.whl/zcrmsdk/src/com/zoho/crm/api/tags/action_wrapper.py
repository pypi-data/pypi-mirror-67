from ..util import Model

from .action_handler import ActionHandler

class ActionWrapper(Model, ActionHandler):
	def __init__(self):
		self.__tags = None
		self.__key_modified = dict()

	def get_tags(self):
		return self.__tags

	def set_tags(self, tags):
		self.__tags = tags
		self.__key_modified["tags"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
