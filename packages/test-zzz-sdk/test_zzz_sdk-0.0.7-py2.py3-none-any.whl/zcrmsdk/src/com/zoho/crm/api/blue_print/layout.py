from ..util import Model


class Layout(Model):
	def __init__(self):
		self.__view = None
		self.__edit = None
		self.__create = None
		self.__quick_create = None
		self.__key_modified = dict()

	def get_view(self):
		return self.__view

	def set_view(self, view):
		self.__view = view
		self.__key_modified["view"] = 1

	def get_edit(self):
		return self.__edit

	def set_edit(self, edit):
		self.__edit = edit
		self.__key_modified["edit"] = 1

	def get_create(self):
		return self.__create

	def set_create(self, create):
		self.__create = create
		self.__key_modified["create"] = 1

	def get_quick_create(self):
		return self.__quick_create

	def set_quick_create(self, quick_create):
		self.__quick_create = quick_create
		self.__key_modified["quick_create"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
