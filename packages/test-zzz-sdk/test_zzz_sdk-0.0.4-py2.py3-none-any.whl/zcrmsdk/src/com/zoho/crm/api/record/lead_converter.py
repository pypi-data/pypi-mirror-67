from ..util import Model


class LeadConverter(Model):
	def __init__(self):
		self.__overwrite = None
		self.__notify_lead_owner = None
		self.__notify_new_entity_owner = None
		self.__accounts = None
		self.__contacts = None
		self.__assign_to = None
		self.__deals = None
		self.__key_modified = dict()

	def get_overwrite(self):
		return self.__overwrite

	def set_overwrite(self, overwrite):
		self.__overwrite = overwrite
		self.__key_modified["overwrite"] = 1

	def get_notify_lead_owner(self):
		return self.__notify_lead_owner

	def set_notify_lead_owner(self, notify_lead_owner):
		self.__notify_lead_owner = notify_lead_owner
		self.__key_modified["notify_lead_owner"] = 1

	def get_notify_new_entity_owner(self):
		return self.__notify_new_entity_owner

	def set_notify_new_entity_owner(self, notify_new_entity_owner):
		self.__notify_new_entity_owner = notify_new_entity_owner
		self.__key_modified["notify_new_entity_owner"] = 1

	def get_accounts(self):
		return self.__accounts

	def set_accounts(self, accounts):
		self.__accounts = accounts
		self.__key_modified["Accounts"] = 1

	def get_contacts(self):
		return self.__contacts

	def set_contacts(self, contacts):
		self.__contacts = contacts
		self.__key_modified["Contacts"] = 1

	def get_assign_to(self):
		return self.__assign_to

	def set_assign_to(self, assign_to):
		self.__assign_to = assign_to
		self.__key_modified["assign_to"] = 1

	def get_deals(self):
		return self.__deals

	def set_deals(self, deals):
		self.__deals = deals
		self.__key_modified["Deals"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
