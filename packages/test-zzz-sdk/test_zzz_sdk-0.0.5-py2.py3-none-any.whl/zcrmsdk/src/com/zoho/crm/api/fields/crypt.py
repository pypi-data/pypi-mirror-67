from ..util import Model


class Crypt(Model):
	def __init__(self):
		self.__mode = None
		self.__column = None
		self.__table = None
		self.__status = None
		self.__key_modified = dict()

	def get_mode(self):
		return self.__mode

	def set_mode(self, mode):
		self.__mode = mode
		self.__key_modified["mode"] = 1

	def get_column(self):
		return self.__column

	def set_column(self, column):
		self.__column = column
		self.__key_modified["column"] = 1

	def get_table(self):
		return self.__table

	def set_table(self, table):
		self.__table = table
		self.__key_modified["table"] = 1

	def get_status(self):
		return self.__status

	def set_status(self, status):
		self.__status = status
		self.__key_modified["status"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
