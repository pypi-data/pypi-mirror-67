from ..util import Model


class User(Model):
	def __init__(self):
		self.__name = None
		self.__id = None
		self.__country = None
		self.__city = None
		self.__signature = None
		self.__name_format = None
		self.__language = None
		self.__locale = None
		self.__personal_account = None
		self.__default_tab_group = None
		self.__street = None
		self.__alias = None
		self.__state = None
		self.__country_locale = None
		self.__first_name = None
		self.__email = None
		self.__zip = None
		self.__decimal_separator = None
		self.__website = None
		self.__time_format = None
		self.__mobile = None
		self.__last_name = None
		self.__time_zone = None
		self.__zuid = None
		self.__confirm = None
		self.__full_name = None
		self.__phone = None
		self.__dob = None
		self.__date_format = None
		self.__status = None
		self.__microsoft = None
		self.__isonline = None
		self.__currency = None
		self.__offset = None
		self.__profile = None
		self.__role = None
		self.__territories = None
		self.__theme = None
		self.__customize_info = None
		self.__key_modified = dict()

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		self.__key_modified["name"] = 1

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

	def get_city(self):
		return self.__city

	def set_city(self, city):
		self.__city = city
		self.__key_modified["city"] = 1

	def get_signature(self):
		return self.__signature

	def set_signature(self, signature):
		self.__signature = signature
		self.__key_modified["signature"] = 1

	def get_name_format(self):
		return self.__name_format

	def set_name_format(self, name_format):
		self.__name_format = name_format
		self.__key_modified["name_format"] = 1

	def get_language(self):
		return self.__language

	def set_language(self, language):
		self.__language = language
		self.__key_modified["language"] = 1

	def get_locale(self):
		return self.__locale

	def set_locale(self, locale):
		self.__locale = locale
		self.__key_modified["locale"] = 1

	def get_personal_account(self):
		return self.__personal_account

	def set_personal_account(self, personal_account):
		self.__personal_account = personal_account
		self.__key_modified["personal_account"] = 1

	def get_default_tab_group(self):
		return self.__default_tab_group

	def set_default_tab_group(self, default_tab_group):
		self.__default_tab_group = default_tab_group
		self.__key_modified["default_tab_group"] = 1

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

	def get_state(self):
		return self.__state

	def set_state(self, state):
		self.__state = state
		self.__key_modified["state"] = 1

	def get_country_locale(self):
		return self.__country_locale

	def set_country_locale(self, country_locale):
		self.__country_locale = country_locale
		self.__key_modified["country_locale"] = 1

	def get_first_name(self):
		return self.__first_name

	def set_first_name(self, first_name):
		self.__first_name = first_name
		self.__key_modified["first_name"] = 1

	def get_email(self):
		return self.__email

	def set_email(self, email):
		self.__email = email
		self.__key_modified["email"] = 1

	def get_zip(self):
		return self.__zip

	def set_zip(self, zip):
		self.__zip = zip
		self.__key_modified["zip"] = 1

	def get_decimal_separator(self):
		return self.__decimal_separator

	def set_decimal_separator(self, decimal_separator):
		self.__decimal_separator = decimal_separator
		self.__key_modified["decimal_separator"] = 1

	def get_website(self):
		return self.__website

	def set_website(self, website):
		self.__website = website
		self.__key_modified["website"] = 1

	def get_time_format(self):
		return self.__time_format

	def set_time_format(self, time_format):
		self.__time_format = time_format
		self.__key_modified["time_format"] = 1

	def get_mobile(self):
		return self.__mobile

	def set_mobile(self, mobile):
		self.__mobile = mobile
		self.__key_modified["mobile"] = 1

	def get_last_name(self):
		return self.__last_name

	def set_last_name(self, last_name):
		self.__last_name = last_name
		self.__key_modified["last_name"] = 1

	def get_time_zone(self):
		return self.__time_zone

	def set_time_zone(self, time_zone):
		self.__time_zone = time_zone
		self.__key_modified["time_zone"] = 1

	def get_zuid(self):
		return self.__zuid

	def set_zuid(self, zuid):
		self.__zuid = zuid
		self.__key_modified["zuid"] = 1

	def get_confirm(self):
		return self.__confirm

	def set_confirm(self, confirm):
		self.__confirm = confirm
		self.__key_modified["confirm"] = 1

	def get_full_name(self):
		return self.__full_name

	def set_full_name(self, full_name):
		self.__full_name = full_name
		self.__key_modified["full_name"] = 1

	def get_phone(self):
		return self.__phone

	def set_phone(self, phone):
		self.__phone = phone
		self.__key_modified["phone"] = 1

	def get_dob(self):
		return self.__dob

	def set_dob(self, dob):
		self.__dob = dob
		self.__key_modified["dob"] = 1

	def get_date_format(self):
		return self.__date_format

	def set_date_format(self, date_format):
		self.__date_format = date_format
		self.__key_modified["date_format"] = 1

	def get_status(self):
		return self.__status

	def set_status(self, status):
		self.__status = status
		self.__key_modified["status"] = 1

	def get_microsoft(self):
		return self.__microsoft

	def set_microsoft(self, microsoft):
		self.__microsoft = microsoft
		self.__key_modified["microsoft"] = 1

	def get_isonline(self):
		return self.__isonline

	def set_isonline(self, isonline):
		self.__isonline = isonline
		self.__key_modified["Isonline"] = 1

	def get_currency(self):
		return self.__currency

	def set_currency(self, currency):
		self.__currency = currency
		self.__key_modified["Currency"] = 1

	def get_offset(self):
		return self.__offset

	def set_offset(self, offset):
		self.__offset = offset
		self.__key_modified["offset"] = 1

	def get_profile(self):
		return self.__profile

	def set_profile(self, profile):
		self.__profile = profile
		self.__key_modified["profile"] = 1

	def get_role(self):
		return self.__role

	def set_role(self, role):
		self.__role = role
		self.__key_modified["role"] = 1

	def get_territories(self):
		return self.__territories

	def set_territories(self, territories):
		self.__territories = territories
		self.__key_modified["territories"] = 1

	def get_theme(self):
		return self.__theme

	def set_theme(self, theme):
		self.__theme = theme
		self.__key_modified["theme"] = 1

	def get_customize_info(self):
		return self.__customize_info

	def set_customize_info(self, customize_info):
		self.__customize_info = customize_info
		self.__key_modified["customize_info"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
