from ..util import Model


class TabTheme(Model):
	def __init__(self):
		self.__font_color = None
		self.__background = None
		self.__key_modified = dict()

	def get_font_color(self):
		return self.__font_color

	def set_font_color(self, font_color):
		self.__font_color = font_color
		self.__key_modified["font_color"] = 1

	def get_background(self):
		return self.__background

	def set_background(self, background):
		self.__background = background
		self.__key_modified["background"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
