from ..util import Model

from .convert_action_response import ConvertActionResponse

class SuccessConvert(Model, ConvertActionResponse):
	def __init__(self):
		self.__contacts = None
		self.__deals = None
		self.__accounts = None
		self.__key_modified = dict()

	def get_contacts(self):
		return self.__contacts

	def set_contacts(self, contacts):
		self.__contacts = contacts
		self.__key_modified["Contacts"] = 1

	def get_deals(self):
		return self.__deals

	def set_deals(self, deals):
		self.__deals = deals
		self.__key_modified["Deals"] = 1

	def get_accounts(self):
		return self.__accounts

	def set_accounts(self, accounts):
		self.__accounts = accounts
		self.__key_modified["Accounts"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
