from ..util import Model


class Translation(Model):
	def __init__(self):
		self.__public_views = None
		self.__other_users_views = None
		self.__shared_with_me = None
		self.__created_by_me = None
		self.__key_modified = dict()

	def get_public_views(self):
		return self.__public_views

	def set_public_views(self, public_views):
		self.__public_views = public_views
		self.__key_modified["public_views"] = 1

	def get_other_users_views(self):
		return self.__other_users_views

	def set_other_users_views(self, other_users_views):
		self.__other_users_views = other_users_views
		self.__key_modified["other_users_views"] = 1

	def get_shared_with_me(self):
		return self.__shared_with_me

	def set_shared_with_me(self, shared_with_me):
		self.__shared_with_me = shared_with_me
		self.__key_modified["shared_with_me"] = 1

	def get_created_by_me(self):
		return self.__created_by_me

	def set_created_by_me(self, created_by_me):
		self.__created_by_me = created_by_me
		self.__key_modified["created_by_me"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
