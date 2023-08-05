from ..fields import Field
from ..util import Model


class Section(Model):
	def __init__(self):
		self.__display_label = None
		self.__api_name = None
		self.__name = None
		self.__generated_type = None
		self.__sequence_number = None
		self.__column_count = None
		self.__tab_traversal = None
		self.__issubformsection = None
		self.__fields = None
		self.__properties = None
		self.__key_modified = dict()

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

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_generated_type(self):
		return self.__generated_type

	def set_generated_type(self, generated_type):
		self.__generated_type = generated_type
		self.__key_modified["generated_type"] = 1

	def get_sequence_number(self):
		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		self.__sequence_number = sequence_number
		self.__key_modified["sequence_number"] = 1

	def get_column_count(self):
		return self.__column_count

	def set_column_count(self, column_count):
		self.__column_count = column_count
		self.__key_modified["column_count"] = 1

	def get_tab_traversal(self):
		return self.__tab_traversal

	def set_tab_traversal(self, tab_traversal):
		self.__tab_traversal = tab_traversal
		self.__key_modified["tab_traversal"] = 1

	def get_issubformsection(self):
		return self.__issubformsection

	def set_issubformsection(self, issubformsection):
		self.__issubformsection = issubformsection
		self.__key_modified["isSubformSection"] = 1

	def get_fields(self):
		return self.__fields

	def set_fields(self, fields):
		self.__fields = fields
		self.__key_modified["fields"] = 1

	def get_properties(self):
		return self.__properties

	def set_properties(self, properties):
		self.__properties = properties
		self.__key_modified["properties"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
