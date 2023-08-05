from ..util import Model


class ProcessInfo(Model):
	def __init__(self):
		self.__field_id = None
		self.__is_continuous = None
		self.__api_name = None
		self.__continuous = None
		self.__field_label = None
		self.__name = None
		self.__column_name = None
		self.__field_value = None
		self.__id = None
		self.__field_name = None
		self.__key_modified = dict()

	def get_field_id(self):
		return self.__field_id

	def set_field_id(self, field_id):
		self.__field_id = field_id
		self.__key_modified["field_id"] = 1

	def get_is_continuous(self):
		return self.__is_continuous

	def set_is_continuous(self, is_continuous):
		self.__is_continuous = is_continuous
		self.__key_modified["is_continuous"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_continuous(self):
		return self.__continuous

	def set_continuous(self, continuous):
		self.__continuous = continuous
		self.__key_modified["continuous"] = 1

	def get_field_label(self):
		return self.__field_label

	def set_field_label(self, field_label):
		self.__field_label = field_label
		self.__key_modified["field_label"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_column_name(self):
		return self.__column_name

	def set_column_name(self, column_name):
		self.__column_name = column_name
		self.__key_modified["column_name"] = 1

	def get_field_value(self):
		return self.__field_value

	def set_field_value(self, field_value):
		self.__field_value = field_value
		self.__key_modified["field_value"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_field_name(self):
		return self.__field_name

	def set_field_name(self, field_name):
		self.__field_name = field_name
		self.__key_modified["field_name"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
