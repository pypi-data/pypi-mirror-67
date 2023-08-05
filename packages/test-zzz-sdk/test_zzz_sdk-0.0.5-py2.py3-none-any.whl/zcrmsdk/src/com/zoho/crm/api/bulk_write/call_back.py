from ..util import Model


class CallBack(Model):
	def __init__(self):
		self.__url = None
		self.__post = None
		self.__key_modified = dict()

	def get_url(self):
		return self.__url

	def set_url(self, url):
		self.__url = url
		self.__key_modified["url"] = 1

	def get_post(self):
		return self.__post

	def set_post(self, post):
		self.__post = post
		self.__key_modified["post"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
