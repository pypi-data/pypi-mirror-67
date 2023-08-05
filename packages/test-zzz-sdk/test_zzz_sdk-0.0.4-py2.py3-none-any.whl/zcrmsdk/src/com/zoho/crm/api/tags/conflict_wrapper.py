from ..util import Model


class ConflictWrapper(Model):
	def __init__(self):
		self.__conflict_id = None
		self.__key_modified = dict()

	def get_conflict_id(self):
		return self.__conflict_id

	def set_conflict_id(self, conflict_id):
		self.__conflict_id = conflict_id
		self.__key_modified["conflict_id"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
