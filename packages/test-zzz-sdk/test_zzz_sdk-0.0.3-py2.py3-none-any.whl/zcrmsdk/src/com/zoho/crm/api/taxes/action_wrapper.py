from ..util import Model

from .action_handler import ActionHandler

class ActionWrapper(Model, ActionHandler):
	def __init__(self):
		self.__taxes = None
		self.__key_modified = dict()

	def get_taxes(self):
		return self.__taxes

	def set_taxes(self, taxes):
		self.__taxes = taxes
		self.__key_modified["taxes"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
