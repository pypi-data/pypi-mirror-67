from ..util import Model


class CustomizeInfo(Model):
	def __init__(self):
		self.__notes_desc = None
		self.__show_right_panel = None
		self.__unpin_recent_item = None
		self.__bc_view = None
		self.__show_home = None
		self.__show_detail_view = None
		self.__key_modified = dict()

	def get_notes_desc(self):
		return self.__notes_desc

	def set_notes_desc(self, notes_desc):
		self.__notes_desc = notes_desc
		self.__key_modified["notes_desc"] = 1

	def get_show_right_panel(self):
		return self.__show_right_panel

	def set_show_right_panel(self, show_right_panel):
		self.__show_right_panel = show_right_panel
		self.__key_modified["show_right_panel"] = 1

	def get_unpin_recent_item(self):
		return self.__unpin_recent_item

	def set_unpin_recent_item(self, unpin_recent_item):
		self.__unpin_recent_item = unpin_recent_item
		self.__key_modified["unpin_recent_item"] = 1

	def get_bc_view(self):
		return self.__bc_view

	def set_bc_view(self, bc_view):
		self.__bc_view = bc_view
		self.__key_modified["bc_view"] = 1

	def get_show_home(self):
		return self.__show_home

	def set_show_home(self, show_home):
		self.__show_home = show_home
		self.__key_modified["show_home"] = 1

	def get_show_detail_view(self):
		return self.__show_detail_view

	def set_show_detail_view(self, show_detail_view):
		self.__show_detail_view = show_detail_view
		self.__key_modified["show_detail_view"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
