from ..util import Model


class LicenseDetails(Model):
	def __init__(self):
		self.__paid_expiry = None
		self.__users_license_purchased = None
		self.__trial_type = None
		self.__trial_expiry = None
		self.__paid = None
		self.__paid_type = None
		self.__key_modified = dict()

	def get_paid_expiry(self):
		return self.__paid_expiry

	def set_paid_expiry(self, paid_expiry):
		self.__paid_expiry = paid_expiry
		self.__key_modified["paid_expiry"] = 1

	def get_users_license_purchased(self):
		return self.__users_license_purchased

	def set_users_license_purchased(self, users_license_purchased):
		self.__users_license_purchased = users_license_purchased
		self.__key_modified["users_license_purchased"] = 1

	def get_trial_type(self):
		return self.__trial_type

	def set_trial_type(self, trial_type):
		self.__trial_type = trial_type
		self.__key_modified["trial_type"] = 1

	def get_trial_expiry(self):
		return self.__trial_expiry

	def set_trial_expiry(self, trial_expiry):
		self.__trial_expiry = trial_expiry
		self.__key_modified["trial_expiry"] = 1

	def get_paid(self):
		return self.__paid

	def set_paid(self, paid):
		self.__paid = paid
		self.__key_modified["paid"] = 1

	def get_paid_type(self):
		return self.__paid_type

	def set_paid_type(self, paid_type):
		self.__paid_type = paid_type
		self.__key_modified["paid_type"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
