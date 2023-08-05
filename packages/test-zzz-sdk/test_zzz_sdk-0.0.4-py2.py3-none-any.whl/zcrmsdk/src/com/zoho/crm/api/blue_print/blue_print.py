from ..util import Model


class BluePrint(Model):
	def __init__(self):
		self.__process_info = None
		self.__transitions = None
		self.__key_modified = dict()

	def get_process_info(self):
		return self.__process_info

	def set_process_info(self, process_info):
		self.__process_info = process_info
		self.__key_modified["process_info"] = 1

	def get_transitions(self):
		return self.__transitions

	def set_transitions(self, transitions):
		self.__transitions = transitions
		self.__key_modified["transitions"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
