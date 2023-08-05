from ..util import Model


class Theme(Model):
	def __init__(self):
		self.__background = None
		self.__new_background = None
		self.__screen = None
		self.__type = None
		self.__normal_tab = None
		self.__selected_tab = None
		self.__key_modified = dict()

	def get_background(self):
		return self.__background

	def set_background(self, background):
		self.__background = background
		self.__key_modified["background"] = 1

	def get_new_background(self):
		return self.__new_background

	def set_new_background(self, new_background):
		self.__new_background = new_background
		self.__key_modified["new_background"] = 1

	def get_screen(self):
		return self.__screen

	def set_screen(self, screen):
		self.__screen = screen
		self.__key_modified["screen"] = 1

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type
		self.__key_modified["type"] = 1

	def get_normal_tab(self):
		return self.__normal_tab

	def set_normal_tab(self, normal_tab):
		self.__normal_tab = normal_tab
		self.__key_modified["normal_tab"] = 1

	def get_selected_tab(self):
		return self.__selected_tab

	def set_selected_tab(self, selected_tab):
		self.__selected_tab = selected_tab
		self.__key_modified["selected_tab"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
