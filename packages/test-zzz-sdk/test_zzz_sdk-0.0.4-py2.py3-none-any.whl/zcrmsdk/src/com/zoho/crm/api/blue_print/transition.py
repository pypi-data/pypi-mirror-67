from ..record import Record
from ..util import Model


class Transition(Model):
	def __init__(self):
		self.__next_transitions = None
		self.__percent_partial_save = None
		self.__data = None
		self.__next_field_value = None
		self.__name = None
		self.__criteria_matched = None
		self.__id = None
		self.__fields = None
		self.__criteria_message = None
		self.__key_modified = dict()

	def get_next_transitions(self):
		return self.__next_transitions

	def set_next_transitions(self, next_transitions):
		self.__next_transitions = next_transitions
		self.__key_modified["next_transitions"] = 1

	def get_percent_partial_save(self):
		return self.__percent_partial_save

	def set_percent_partial_save(self, percent_partial_save):
		self.__percent_partial_save = percent_partial_save
		self.__key_modified["percent_partial_save"] = 1

	def get_data(self):
		return self.__data

	def set_data(self, data):
		self.__data = data
		self.__key_modified["data"] = 1

	def get_next_field_value(self):
		return self.__next_field_value

	def set_next_field_value(self, next_field_value):
		self.__next_field_value = next_field_value
		self.__key_modified["next_field_value"] = 1

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

	def get_criteria_matched(self):
		return self.__criteria_matched

	def set_criteria_matched(self, criteria_matched):
		self.__criteria_matched = criteria_matched
		self.__key_modified["criteria_matched"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_fields(self):
		return self.__fields

	def set_fields(self, fields):
		self.__fields = fields
		self.__key_modified["fields"] = 1

	def get_criteria_message(self):
		return self.__criteria_message

	def set_criteria_message(self, criteria_message):
		self.__criteria_message = criteria_message
		self.__key_modified["criteria_message"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
