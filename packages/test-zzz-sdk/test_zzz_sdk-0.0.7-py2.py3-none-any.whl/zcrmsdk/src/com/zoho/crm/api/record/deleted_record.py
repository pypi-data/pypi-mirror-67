from ..users import User
from ..util import Model

from .deleted_records_response import DeletedRecordsResponse

class DeletedRecord(Model, DeletedRecordsResponse):
	def __init__(self):
		self.__deleted_by = None
		self.__created_by = None
		self.__id = None
		self.__display_name = None
		self.__type = None
		self.__deleted_time = None
		self.__key_modified = dict()

	def get_deleted_by(self):
		return self.__deleted_by

	def set_deleted_by(self, deleted_by):
		self.__deleted_by = deleted_by
		self.__key_modified["deleted_by"] = 1

	def get_created_by(self):
		return self.__created_by

	def set_created_by(self, created_by):
		self.__created_by = created_by
		self.__key_modified["created_by"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_display_name(self):
		return self.__display_name

	def set_display_name(self, display_name):
		self.__display_name = display_name
		self.__key_modified["display_name"] = 1

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type
		self.__key_modified["type"] = 1

	def get_deleted_time(self):
		return self.__deleted_time

	def set_deleted_time(self, deleted_time):
		self.__deleted_time = deleted_time
		self.__key_modified["deleted_time"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
