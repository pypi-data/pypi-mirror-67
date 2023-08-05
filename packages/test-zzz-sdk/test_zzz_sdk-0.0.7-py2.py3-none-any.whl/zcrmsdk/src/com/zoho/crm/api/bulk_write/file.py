from ..util import Model


class File(Model):
	def __init__(self):
		self.__status = None
		self.__name = None
		self.__added_count = None
		self.__skipped_count = None
		self.__updated_count = None
		self.__total_count = None
		self.__key_modified = dict()

	def get_status(self):
		return self.__status

	def set_status(self, status):
		self.__status = status
		self.__key_modified["status"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_added_count(self):
		return self.__added_count

	def set_added_count(self, added_count):
		self.__added_count = added_count
		self.__key_modified["added_count"] = 1

	def get_skipped_count(self):
		return self.__skipped_count

	def set_skipped_count(self, skipped_count):
		self.__skipped_count = skipped_count
		self.__key_modified["skipped_count"] = 1

	def get_updated_count(self):
		return self.__updated_count

	def set_updated_count(self, updated_count):
		self.__updated_count = updated_count
		self.__key_modified["updated_count"] = 1

	def get_total_count(self):
		return self.__total_count

	def set_total_count(self, total_count):
		self.__total_count = total_count
		self.__key_modified["total_count"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
