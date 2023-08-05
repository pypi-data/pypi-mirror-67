from ..util import Model


class RelatedList(Model):
	def __init__(self):
		self.__id = None
		self.__sequence_number = None
		self.__display_label = None
		self.__api_name = None
		self.__module = None
		self.__name = None
		self.__action = None
		self.__href = None
		self.__type = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_sequence_number(self):
		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		self.__sequence_number = sequence_number
		self.__key_modified["sequence_number"] = 1

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_module(self):
		return self.__module

	def set_module(self, module):
		self.__module = module
		self.__key_modified["module"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_action(self):
		return self.__action

	def set_action(self, action):
		self.__action = action
		self.__key_modified["action"] = 1

	def get_href(self):
		return self.__href

	def set_href(self, href):
		self.__href = href
		self.__key_modified["href"] = 1

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type
		self.__key_modified["type"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
