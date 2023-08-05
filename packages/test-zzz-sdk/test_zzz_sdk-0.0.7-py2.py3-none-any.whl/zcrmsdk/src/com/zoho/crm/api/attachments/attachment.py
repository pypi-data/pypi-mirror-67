from ..record import Record
from ..users import User
from ..util import Model


class Attachment(Model):
	def __init__(self):
		self.__owner = None
		self.__modified_time = None
		self.__file_name = None
		self.__created_time = None
		self.__size = None
		self.__parent_id = None
		self.__editable = None
		self.__file_id = None
		self.__type = None
		self.__se_module = None
		self.__modified_by = None
		self.__state = None
		self.__id = None
		self.__created_by = None
		self.__link_url = None
		self.__description = None
		self.__category = None
		self.__key_modified = dict()

	def get_owner(self):
		return self.__owner

	def set_owner(self, owner):
		self.__owner = owner
		self.__key_modified["Owner"] = 1

	def get_modified_time(self):
		return self.__modified_time

	def set_modified_time(self, modified_time):
		self.__modified_time = modified_time
		self.__key_modified["Modified_Time"] = 1

	def get_file_name(self):
		return self.__file_name

	def set_file_name(self, file_name):
		self.__file_name = file_name
		self.__key_modified["File_Name"] = 1

	def get_created_time(self):
		return self.__created_time

	def set_created_time(self, created_time):
		self.__created_time = created_time
		self.__key_modified["Created_Time"] = 1

	def get_size(self):
		return self.__size

	def set_size(self, size):
		self.__size = size
		self.__key_modified["Size"] = 1

	def get_parent_id(self):
		return self.__parent_id

	def set_parent_id(self, parent_id):
		self.__parent_id = parent_id
		self.__key_modified["Parent_Id"] = 1

	def get_editable(self):
		return self.__editable

	def set_editable(self, editable):
		self.__editable = editable
		self.__key_modified["$editable"] = 1

	def get_file_id(self):
		return self.__file_id

	def set_file_id(self, file_id):
		self.__file_id = file_id
		self.__key_modified["$file_id"] = 1

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type
		self.__key_modified["$type"] = 1

	def get_se_module(self):
		return self.__se_module

	def set_se_module(self, se_module):
		self.__se_module = se_module
		self.__key_modified["$se_module"] = 1

	def get_modified_by(self):
		return self.__modified_by

	def set_modified_by(self, modified_by):
		self.__modified_by = modified_by
		self.__key_modified["Modified_By"] = 1

	def get_state(self):
		return self.__state

	def set_state(self, state):
		self.__state = state
		self.__key_modified["$state"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_created_by(self):
		return self.__created_by

	def set_created_by(self, created_by):
		self.__created_by = created_by
		self.__key_modified["Created_By"] = 1

	def get_link_url(self):
		return self.__link_url

	def set_link_url(self, link_url):
		self.__link_url = link_url
		self.__key_modified["$link_url"] = 1

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description
		self.__key_modified["description"] = 1

	def get_category(self):
		return self.__category

	def set_category(self, category):
		self.__category = category
		self.__key_modified["category"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
