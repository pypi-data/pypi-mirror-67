from ..util import Model


class Preference(Model):
	def __init__(self):
		self.__auto_populate_tax = None
		self.__modify_tax_rates = None
		self.__key_modified = dict()

	def get_auto_populate_tax(self):
		return self.__auto_populate_tax

	def set_auto_populate_tax(self, auto_populate_tax):
		self.__auto_populate_tax = auto_populate_tax
		self.__key_modified["auto_populate_tax"] = 1

	def get_modify_tax_rates(self):
		return self.__modify_tax_rates

	def set_modify_tax_rates(self, modify_tax_rates):
		self.__modify_tax_rates = modify_tax_rates
		self.__key_modified["modify_tax_rates"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
