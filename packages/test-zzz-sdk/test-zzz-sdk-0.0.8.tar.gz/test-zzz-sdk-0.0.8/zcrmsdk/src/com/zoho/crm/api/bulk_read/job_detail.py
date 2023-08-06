from ..users import User
from ..util import Model


class JobDetail(Model):
	def __init__(self):
		self.__id = None
		self.__operation = None
		self.__state = None
		self.__query = None
		self.__created_by = None
		self.__created_time = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string value
		"""
		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string value
		"""
		self.__id = id
		self.__key_modified["id"] = 1

	def get_operation(self):
		"""
		The method to get the operation

		Returns:
			string: A string value
		"""
		return self.__operation

	def set_operation(self, operation):
		"""
		The method to set the value to operation

		Parameters:
			operation (string) : A string value
		"""
		self.__operation = operation
		self.__key_modified["operation"] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string value
		"""
		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string value
		"""
		self.__state = state
		self.__key_modified["state"] = 1

	def get_query(self):
		"""
		The method to get the query

		Returns:
			dict: An instance of dict
		"""
		return self.__query

	def set_query(self, query):
		"""
		The method to set the value to query

		Parameters:
			query (dict) : An instance of dict
		"""
		self.__query = query
		self.__key_modified["query"] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""
		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""
		self.__created_by = created_by
		self.__key_modified["created_by"] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			DateTime: An instance of DateTime
		"""
		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (DateTime) : An instance of DateTime
		"""
		self.__created_time = created_time
		self.__key_modified["created_time"] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string value

		Returns:
			int: A int value
		"""
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		"""
		The method to mark the given key as modified

		Parameters:
			modification (int) : A int value
			key (string) : A string value
		"""
		self.__key_modified[key] = modification
