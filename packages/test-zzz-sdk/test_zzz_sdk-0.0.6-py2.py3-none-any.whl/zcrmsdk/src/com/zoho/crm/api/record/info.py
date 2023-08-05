from ..util import Model


class Info(Model):
	def __init__(self):
		self.__per_page = None
		self.__count = None
		self.__page = None
		self.__more_records = None
		self.__key_modified = dict()

	def get_per_page(self):
		return self.__per_page

	def set_per_page(self, per_page):
		self.__per_page = per_page
		self.__key_modified["per_page"] = 1

	def get_count(self):
		return self.__count

	def set_count(self, count):
		self.__count = count
		self.__key_modified["count"] = 1

	def get_page(self):
		return self.__page

	def set_page(self, page):
		self.__page = page
		self.__key_modified["page"] = 1

	def get_more_records(self):
		return self.__more_records

	def set_more_records(self, more_records):
		self.__more_records = more_records
		self.__key_modified["more_records"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
