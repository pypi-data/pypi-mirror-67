from ..profile import Profile
from ..users import User
from ..util import Model


class Layout(Model):
	def __init__(self):
		self.__id = None
		self.__name = None
		self.__status = None
		self.__modified_time = None
		self.__created_for = None
		self.__created_by = None
		self.__modified_by = None
		self.__profiles = None
		self.__sections = None
		self.__visible = None
		self.__convert_mapping = None
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

	def get_status(self):
		return self.__status

	def set_status(self, status):
		self.__status = status
		self.__key_modified["status"] = 1

	def get_modified_time(self):
		return self.__modified_time

	def set_modified_time(self, modified_time):
		self.__modified_time = modified_time
		self.__key_modified["modified_time"] = 1

	def get_created_for(self):
		return self.__created_for

	def set_created_for(self, created_for):
		self.__created_for = created_for
		self.__key_modified["created_for"] = 1

	def get_created_by(self):
		return self.__created_by

	def set_created_by(self, created_by):
		self.__created_by = created_by
		self.__key_modified["created_by"] = 1

	def get_modified_by(self):
		return self.__modified_by

	def set_modified_by(self, modified_by):
		self.__modified_by = modified_by
		self.__key_modified["modified_by"] = 1

	def get_profiles(self):
		return self.__profiles

	def set_profiles(self, profiles):
		self.__profiles = profiles
		self.__key_modified["profiles"] = 1

	def get_sections(self):
		return self.__sections

	def set_sections(self, sections):
		self.__sections = sections
		self.__key_modified["sections"] = 1

	def get_visible(self):
		return self.__visible

	def set_visible(self, visible):
		self.__visible = visible
		self.__key_modified["visible"] = 1

	def get_convert_mapping(self):
		return self.__convert_mapping

	def set_convert_mapping(self, convert_mapping):
		self.__convert_mapping = convert_mapping
		self.__key_modified["convert_mapping"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
