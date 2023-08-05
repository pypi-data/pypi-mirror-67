from ..util import Model

from .record_action_response import RecordActionResponse

class MultipleRecordSuccessResponse(Model, RecordActionResponse):
	def __init__(self):
		self.__data = None
		self.__wf_scheduler = None
		self.__success_count = None
		self.__locked_count = None
		self.__key_modified = dict()

	def get_data(self):
		return self.__data

	def set_data(self, data):
		self.__data = data
		self.__key_modified["data"] = 1

	def get_wf_scheduler(self):
		return self.__wf_scheduler

	def set_wf_scheduler(self, wf_scheduler):
		self.__wf_scheduler = wf_scheduler
		self.__key_modified["wf_scheduler"] = 1

	def get_success_count(self):
		return self.__success_count

	def set_success_count(self, success_count):
		self.__success_count = success_count
		self.__key_modified["success_count"] = 1

	def get_locked_count(self):
		return self.__locked_count

	def set_locked_count(self, locked_count):
		self.__locked_count = locked_count
		self.__key_modified["locked_count"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
