from ..util import Model


class MultiSelectLookup(Model):
	def __init__(self):
		self.__display_label = None
		self.__linking_module = None
		self.__lookup_apiname = None
		self.__api_name = None
		self.__connectedlookup_apiname = None
		self.__id = None
		self.__key_modified = dict()

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_linking_module(self):
		return self.__linking_module

	def set_linking_module(self, linking_module):
		self.__linking_module = linking_module
		self.__key_modified["linking_module"] = 1

	def get_lookup_apiname(self):
		return self.__lookup_apiname

	def set_lookup_apiname(self, lookup_apiname):
		self.__lookup_apiname = lookup_apiname
		self.__key_modified["lookup_apiname"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_connectedlookup_apiname(self):
		return self.__connectedlookup_apiname

	def set_connectedlookup_apiname(self, connectedlookup_apiname):
		self.__connectedlookup_apiname = connectedlookup_apiname
		self.__key_modified["connectedlookup_apiname"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
