from ..util import Model


class CustomView(Model):
	def __init__(self):
		self.__id = None
		self.__name = None
		self.__system_name = None
		self.__display_value = None
		self.__shared_type = None
		self.__category = None
		self.__sort_by = None
		self.__sort_order = None
		self.__favorite = None
		self.__offline = None
		self.__default = None
		self.__system_defined = None
		self.__criteria = None
		self.__shared_details = None
		self.__fields = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_system_name(self):
		return self.__system_name

	def set_system_name(self, system_name):
		self.__system_name = system_name
		self.__key_modified["system_name"] = 1

	def get_display_value(self):
		return self.__display_value

	def set_display_value(self, display_value):
		self.__display_value = display_value
		self.__key_modified["display_value"] = 1

	def get_shared_type(self):
		return self.__shared_type

	def set_shared_type(self, shared_type):
		self.__shared_type = shared_type
		self.__key_modified["shared_type"] = 1

	def get_category(self):
		return self.__category

	def set_category(self, category):
		self.__category = category
		self.__key_modified["category"] = 1

	def get_sort_by(self):
		return self.__sort_by

	def set_sort_by(self, sort_by):
		self.__sort_by = sort_by
		self.__key_modified["sort_by"] = 1

	def get_sort_order(self):
		return self.__sort_order

	def set_sort_order(self, sort_order):
		self.__sort_order = sort_order
		self.__key_modified["sort_order"] = 1

	def get_favorite(self):
		return self.__favorite

	def set_favorite(self, favorite):
		self.__favorite = favorite
		self.__key_modified["favorite"] = 1

	def get_offline(self):
		return self.__offline

	def set_offline(self, offline):
		self.__offline = offline
		self.__key_modified["offline"] = 1

	def get_default(self):
		return self.__default

	def set_default(self, default):
		self.__default = default
		self.__key_modified["default"] = 1

	def get_system_defined(self):
		return self.__system_defined

	def set_system_defined(self, system_defined):
		self.__system_defined = system_defined
		self.__key_modified["system_defined"] = 1

	def get_criteria(self):
		return self.__criteria

	def set_criteria(self, criteria):
		self.__criteria = criteria
		self.__key_modified["criteria"] = 1

	def get_shared_details(self):
		return self.__shared_details

	def set_shared_details(self, shared_details):
		self.__shared_details = shared_details
		self.__key_modified["shared_details"] = 1

	def get_fields(self):
		return self.__fields

	def set_fields(self, fields):
		self.__fields = fields
		self.__key_modified["fields"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
