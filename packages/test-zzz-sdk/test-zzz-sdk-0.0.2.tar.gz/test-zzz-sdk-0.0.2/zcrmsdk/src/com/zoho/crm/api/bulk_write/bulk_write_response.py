from ..util import Model


class BulkWriteResponse(Model):
	def __init__(self):
		self.__status = None
		self.__character_encoding = None
		self.__resource = None
		self.__id = None
		self.__result = None
		self.__operation = None
		self.__created_time = None
		self.__key_modified = dict()

	def get_status(self):
		return self.__status

	def set_status(self, status):
		self.__status = status
		self.__key_modified["status"] = 1

	def get_character_encoding(self):
		return self.__character_encoding

	def set_character_encoding(self, character_encoding):
		self.__character_encoding = character_encoding
		self.__key_modified["character_encoding"] = 1

	def get_resource(self):
		return self.__resource

	def set_resource(self, resource):
		self.__resource = resource
		self.__key_modified["resource"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_result(self):
		return self.__result

	def set_result(self, result):
		self.__result = result
		self.__key_modified["result"] = 1

	def get_operation(self):
		return self.__operation

	def set_operation(self, operation):
		self.__operation = operation
		self.__key_modified["operation"] = 1

	def get_created_time(self):
		return self.__created_time

	def set_created_time(self, created_time):
		self.__created_time = created_time
		self.__key_modified["created_time"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
