from ..util import Model


class Org(Model):
	def __init__(self):
		self.__id = None
		self.__country = None
		self.__photo_id = None
		self.__city = None
		self.__description = None
		self.__mc_status = None
		self.__gapps_enabled = None
		self.__translation_enabled = None
		self.__street = None
		self.__alias = None
		self.__currency = None
		self.__state = None
		self.__fax = None
		self.__employee_count = None
		self.__zip = None
		self.__website = None
		self.__currency_symbol = None
		self.__mobile = None
		self.__currency_locale = None
		self.__primary_zuid = None
		self.__zia_portal_id = None
		self.__time_zone = None
		self.__zgid = None
		self.__country_code = None
		self.__phone = None
		self.__company_name = None
		self.__privacy_settings = None
		self.__primary_email = None
		self.__iso_code = None
		self.__license_details = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_country(self):
		return self.__country

	def set_country(self, country):
		self.__country = country
		self.__key_modified["country"] = 1

	def get_photo_id(self):
		return self.__photo_id

	def set_photo_id(self, photo_id):
		self.__photo_id = photo_id
		self.__key_modified["photo_id"] = 1

	def get_city(self):
		return self.__city

	def set_city(self, city):
		self.__city = city
		self.__key_modified["city"] = 1

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description
		self.__key_modified["description"] = 1

	def get_mc_status(self):
		return self.__mc_status

	def set_mc_status(self, mc_status):
		self.__mc_status = mc_status
		self.__key_modified["mc_status"] = 1

	def get_gapps_enabled(self):
		return self.__gapps_enabled

	def set_gapps_enabled(self, gapps_enabled):
		self.__gapps_enabled = gapps_enabled
		self.__key_modified["gapps_enabled"] = 1

	def get_translation_enabled(self):
		return self.__translation_enabled

	def set_translation_enabled(self, translation_enabled):
		self.__translation_enabled = translation_enabled
		self.__key_modified["translation_enabled"] = 1

	def get_street(self):
		return self.__street

	def set_street(self, street):
		self.__street = street
		self.__key_modified["street"] = 1

	def get_alias(self):
		return self.__alias

	def set_alias(self, alias):
		self.__alias = alias
		self.__key_modified["alias"] = 1

	def get_currency(self):
		return self.__currency

	def set_currency(self, currency):
		self.__currency = currency
		self.__key_modified["currency"] = 1

	def get_state(self):
		return self.__state

	def set_state(self, state):
		self.__state = state
		self.__key_modified["state"] = 1

	def get_fax(self):
		return self.__fax

	def set_fax(self, fax):
		self.__fax = fax
		self.__key_modified["fax"] = 1

	def get_employee_count(self):
		return self.__employee_count

	def set_employee_count(self, employee_count):
		self.__employee_count = employee_count
		self.__key_modified["employee_count"] = 1

	def get_zip(self):
		return self.__zip

	def set_zip(self, zip):
		self.__zip = zip
		self.__key_modified["zip"] = 1

	def get_website(self):
		return self.__website

	def set_website(self, website):
		self.__website = website
		self.__key_modified["website"] = 1

	def get_currency_symbol(self):
		return self.__currency_symbol

	def set_currency_symbol(self, currency_symbol):
		self.__currency_symbol = currency_symbol
		self.__key_modified["currency_symbol"] = 1

	def get_mobile(self):
		return self.__mobile

	def set_mobile(self, mobile):
		self.__mobile = mobile
		self.__key_modified["mobile"] = 1

	def get_currency_locale(self):
		return self.__currency_locale

	def set_currency_locale(self, currency_locale):
		self.__currency_locale = currency_locale
		self.__key_modified["currency_locale"] = 1

	def get_primary_zuid(self):
		return self.__primary_zuid

	def set_primary_zuid(self, primary_zuid):
		self.__primary_zuid = primary_zuid
		self.__key_modified["primary_zuid"] = 1

	def get_zia_portal_id(self):
		return self.__zia_portal_id

	def set_zia_portal_id(self, zia_portal_id):
		self.__zia_portal_id = zia_portal_id
		self.__key_modified["zia_portal_id"] = 1

	def get_time_zone(self):
		return self.__time_zone

	def set_time_zone(self, time_zone):
		self.__time_zone = time_zone
		self.__key_modified["time_zone"] = 1

	def get_zgid(self):
		return self.__zgid

	def set_zgid(self, zgid):
		self.__zgid = zgid
		self.__key_modified["zgid"] = 1

	def get_country_code(self):
		return self.__country_code

	def set_country_code(self, country_code):
		self.__country_code = country_code
		self.__key_modified["country_code"] = 1

	def get_phone(self):
		return self.__phone

	def set_phone(self, phone):
		self.__phone = phone
		self.__key_modified["phone"] = 1

	def get_company_name(self):
		return self.__company_name

	def set_company_name(self, company_name):
		self.__company_name = company_name
		self.__key_modified["company_name"] = 1

	def get_privacy_settings(self):
		return self.__privacy_settings

	def set_privacy_settings(self, privacy_settings):
		self.__privacy_settings = privacy_settings
		self.__key_modified["privacy_settings"] = 1

	def get_primary_email(self):
		return self.__primary_email

	def set_primary_email(self, primary_email):
		self.__primary_email = primary_email
		self.__key_modified["primary_email"] = 1

	def get_iso_code(self):
		return self.__iso_code

	def set_iso_code(self, iso_code):
		self.__iso_code = iso_code
		self.__key_modified["iso_code"] = 1

	def get_license_details(self):
		return self.__license_details

	def set_license_details(self, license_details):
		self.__license_details = license_details
		self.__key_modified["license_details"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
