from ..users import User
from ..util import Model


class Role(Model):
	def __init__(self):
		self.__id = None
		self.__name = None
		self.__display_label = None
		self.__admin_user = None
		self.__reporting_to = None
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

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_admin_user(self):
		return self.__admin_user

	def set_admin_user(self, admin_user):
		self.__admin_user = admin_user
		self.__key_modified["admin_user"] = 1

	def get_reporting_to(self):
		return self.__reporting_to

	def set_reporting_to(self, reporting_to):
		self.__reporting_to = reporting_to
		self.__key_modified["reporting_to"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
