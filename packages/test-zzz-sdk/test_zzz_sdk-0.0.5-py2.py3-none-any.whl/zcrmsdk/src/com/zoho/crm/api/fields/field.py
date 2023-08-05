from ..util import Model


class Field(Model):
	def __init__(self):
		self.__id = None
		self.__api_name = None
		self.__system_mandatory = None
		self.__webhook = None
		self.__json_type = None
		self.__crypt = None
		self.__field_label = None
		self.__tooltip = None
		self.__field_read_only = None
		self.__display_label = None
		self.__default_value = None
		self.__decimal_place = None
		self.__quick_sequence_number = None
		self.__section_id = None
		self.__read_only = None
		self.__blueprint_supported = None
		self.__length = None
		self.__custom_field = None
		self.__mass_update = None
		self.__visible = None
		self.__association_details = None
		self.__validation_rule = None
		self.__multi_module_lookup = None
		self.__formula = None
		self.__unique = None
		self.__multiselectlookup = None
		self.__auto_number = None
		self.__businesscard_supported = None
		self.__history_tracking = None
		self.__currency = None
		self.__lookup = None
		self.__subform = None
		self.__convert_mapping = None
		self.__pick_list_values = None
		self.__data_type = None
		self.__key_modified = dict()

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_system_mandatory(self):
		return self.__system_mandatory

	def set_system_mandatory(self, system_mandatory):
		self.__system_mandatory = system_mandatory
		self.__key_modified["system_mandatory"] = 1

	def get_webhook(self):
		return self.__webhook

	def set_webhook(self, webhook):
		self.__webhook = webhook
		self.__key_modified["webhook"] = 1

	def get_json_type(self):
		return self.__json_type

	def set_json_type(self, json_type):
		self.__json_type = json_type
		self.__key_modified["json_type"] = 1

	def get_crypt(self):
		return self.__crypt

	def set_crypt(self, crypt):
		self.__crypt = crypt
		self.__key_modified["crypt"] = 1

	def get_field_label(self):
		return self.__field_label

	def set_field_label(self, field_label):
		self.__field_label = field_label
		self.__key_modified["field_label"] = 1

	def get_tooltip(self):
		return self.__tooltip

	def set_tooltip(self, tooltip):
		self.__tooltip = tooltip
		self.__key_modified["tooltip"] = 1

	def get_field_read_only(self):
		return self.__field_read_only

	def set_field_read_only(self, field_read_only):
		self.__field_read_only = field_read_only
		self.__key_modified["field_read_only"] = 1

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_default_value(self):
		return self.__default_value

	def set_default_value(self, default_value):
		self.__default_value = default_value
		self.__key_modified["default_value"] = 1

	def get_decimal_place(self):
		return self.__decimal_place

	def set_decimal_place(self, decimal_place):
		self.__decimal_place = decimal_place
		self.__key_modified["decimal_place"] = 1

	def get_quick_sequence_number(self):
		return self.__quick_sequence_number

	def set_quick_sequence_number(self, quick_sequence_number):
		self.__quick_sequence_number = quick_sequence_number
		self.__key_modified["quick_sequence_number"] = 1

	def get_section_id(self):
		return self.__section_id

	def set_section_id(self, section_id):
		self.__section_id = section_id
		self.__key_modified["section_id"] = 1

	def get_read_only(self):
		return self.__read_only

	def set_read_only(self, read_only):
		self.__read_only = read_only
		self.__key_modified["read_only"] = 1

	def get_blueprint_supported(self):
		return self.__blueprint_supported

	def set_blueprint_supported(self, blueprint_supported):
		self.__blueprint_supported = blueprint_supported
		self.__key_modified["blueprint_supported"] = 1

	def get_length(self):
		return self.__length

	def set_length(self, length):
		self.__length = length
		self.__key_modified["length"] = 1

	def get_custom_field(self):
		return self.__custom_field

	def set_custom_field(self, custom_field):
		self.__custom_field = custom_field
		self.__key_modified["custom_field"] = 1

	def get_mass_update(self):
		return self.__mass_update

	def set_mass_update(self, mass_update):
		self.__mass_update = mass_update
		self.__key_modified["mass_update"] = 1

	def get_visible(self):
		return self.__visible

	def set_visible(self, visible):
		self.__visible = visible
		self.__key_modified["visible"] = 1

	def get_association_details(self):
		return self.__association_details

	def set_association_details(self, association_details):
		self.__association_details = association_details
		self.__key_modified["association_details"] = 1

	def get_validation_rule(self):
		return self.__validation_rule

	def set_validation_rule(self, validation_rule):
		self.__validation_rule = validation_rule
		self.__key_modified["validation_rule"] = 1

	def get_multi_module_lookup(self):
		return self.__multi_module_lookup

	def set_multi_module_lookup(self, multi_module_lookup):
		self.__multi_module_lookup = multi_module_lookup
		self.__key_modified["multi_module_lookup"] = 1

	def get_formula(self):
		return self.__formula

	def set_formula(self, formula):
		self.__formula = formula
		self.__key_modified["formula"] = 1

	def get_unique(self):
		return self.__unique

	def set_unique(self, unique):
		self.__unique = unique
		self.__key_modified["unique"] = 1

	def get_multiselectlookup(self):
		return self.__multiselectlookup

	def set_multiselectlookup(self, multiselectlookup):
		self.__multiselectlookup = multiselectlookup
		self.__key_modified["multiselectlookup"] = 1

	def get_auto_number(self):
		return self.__auto_number

	def set_auto_number(self, auto_number):
		self.__auto_number = auto_number
		self.__key_modified["auto_number"] = 1

	def get_businesscard_supported(self):
		return self.__businesscard_supported

	def set_businesscard_supported(self, businesscard_supported):
		self.__businesscard_supported = businesscard_supported
		self.__key_modified["businesscard_supported"] = 1

	def get_history_tracking(self):
		return self.__history_tracking

	def set_history_tracking(self, history_tracking):
		self.__history_tracking = history_tracking
		self.__key_modified["history_tracking"] = 1

	def get_currency(self):
		return self.__currency

	def set_currency(self, currency):
		self.__currency = currency
		self.__key_modified["currency"] = 1

	def get_lookup(self):
		return self.__lookup

	def set_lookup(self, lookup):
		self.__lookup = lookup
		self.__key_modified["lookup"] = 1

	def get_subform(self):
		return self.__subform

	def set_subform(self, subform):
		self.__subform = subform
		self.__key_modified["subform"] = 1

	def get_convert_mapping(self):
		return self.__convert_mapping

	def set_convert_mapping(self, convert_mapping):
		self.__convert_mapping = convert_mapping
		self.__key_modified["convert_mapping"] = 1

	def get_pick_list_values(self):
		return self.__pick_list_values

	def set_pick_list_values(self, pick_list_values):
		self.__pick_list_values = pick_list_values
		self.__key_modified["pick_list_values"] = 1

	def get_data_type(self):
		return self.__data_type

	def set_data_type(self, data_type):
		self.__data_type = data_type
		self.__key_modified["data_type"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
