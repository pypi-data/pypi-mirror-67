from ..attachments import Attachment
from ..users import User
from ..util import Model


class Note(Model):
	def __init__(self):
		self.__id = None
		self.__note_title = None
		self.__note_content = None
		self.__modified_time = None
		self.__created_time = None
		self.__parent_id = None
		self.__owner = None
		self.__created_by = None
		self.__modified_by = None
		self.__editable = None
		self.__se_module = None
		self.__is_shared_to_client = None
		self.__size = None
		self.__state = None
		self.__voice_note = None
		self.__attachments = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_note_title(self):
		return self.__note_title

	def set_note_title(self, note_title):
		self.__note_title = note_title
		self.__key_modified["Note_Title"] = 1

	def get_note_content(self):
		return self.__note_content

	def set_note_content(self, note_content):
		self.__note_content = note_content
		self.__key_modified["Note_Content"] = 1

	def get_modified_time(self):
		return self.__modified_time

	def set_modified_time(self, modified_time):
		self.__modified_time = modified_time
		self.__key_modified["Modified_Time"] = 1

	def get_created_time(self):
		return self.__created_time

	def set_created_time(self, created_time):
		self.__created_time = created_time
		self.__key_modified["Created_Time"] = 1

	def get_parent_id(self):
		return self.__parent_id

	def set_parent_id(self, parent_id):
		self.__parent_id = parent_id
		self.__key_modified["Parent_Id"] = 1

	def get_owner(self):
		return self.__owner

	def set_owner(self, owner):
		self.__owner = owner
		self.__key_modified["Owner"] = 1

	def get_created_by(self):
		return self.__created_by

	def set_created_by(self, created_by):
		self.__created_by = created_by
		self.__key_modified["Created_By"] = 1

	def get_modified_by(self):
		return self.__modified_by

	def set_modified_by(self, modified_by):
		self.__modified_by = modified_by
		self.__key_modified["Modified_By"] = 1

	def get_editable(self):
		return self.__editable

	def set_editable(self, editable):
		self.__editable = editable
		self.__key_modified["$editable"] = 1

	def get_se_module(self):
		return self.__se_module

	def set_se_module(self, se_module):
		self.__se_module = se_module
		self.__key_modified["$se_module"] = 1

	def get_is_shared_to_client(self):
		return self.__is_shared_to_client

	def set_is_shared_to_client(self, is_shared_to_client):
		self.__is_shared_to_client = is_shared_to_client
		self.__key_modified["$is_shared_to_client"] = 1

	def get_size(self):
		return self.__size

	def set_size(self, size):
		self.__size = size
		self.__key_modified["$size"] = 1

	def get_state(self):
		return self.__state

	def set_state(self, state):
		self.__state = state
		self.__key_modified["$state"] = 1

	def get_voice_note(self):
		return self.__voice_note

	def set_voice_note(self, voice_note):
		self.__voice_note = voice_note
		self.__key_modified["$voice_note"] = 1

	def get_attachments(self):
		return self.__attachments

	def set_attachments(self, attachments):
		self.__attachments = attachments
		self.__key_modified["$attachments"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
