from ..util import Model


class Field(Model):
	def __init__(self):
		self.__webhook = None
		self.__json_type = None
		self.__display_label = None
		self.__data_type = None
		self.__column_name = None
		self.__personality_name = None
		self.__id = None
		self.__transition_sequence = None
		self.__mandatory = None
		self.__layouts = None
		self.__api_name = None
		self.__content = None
		self.__system_mandatory = None
		self.__crypt = None
		self.__field_label = None
		self.__tooltip = None
		self.__created_source = None
		self.__field_read_only = None
		self.__validation_rule = None
		self.__read_only = None
		self.__association_details = None
		self.__quick_sequence_number = None
		self.__custom_field = None
		self.__visible = None
		self.__length = None
		self.__decimal_place = None
		self.__view_type = None
		self.__pick_list_values = None
		self.__multiselectlookup = None
		self.__auto_number = None
		self.__key_modified = dict()

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

	def get_display_label(self):
		return self.__display_label

	def set_display_label(self, display_label):
		self.__display_label = display_label
		self.__key_modified["display_label"] = 1

	def get_data_type(self):
		return self.__data_type

	def set_data_type(self, data_type):
		self.__data_type = data_type
		self.__key_modified["data_type"] = 1

	def get_column_name(self):
		return self.__column_name

	def set_column_name(self, column_name):
		self.__column_name = column_name
		self.__key_modified["column_name"] = 1

	def get_personality_name(self):
		return self.__personality_name

	def set_personality_name(self, personality_name):
		self.__personality_name = personality_name
		self.__key_modified["personality_name"] = 1

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id
		self.__key_modified["id"] = 1

	def get_transition_sequence(self):
		return self.__transition_sequence

	def set_transition_sequence(self, transition_sequence):
		self.__transition_sequence = transition_sequence
		self.__key_modified["transition_sequence"] = 1

	def get_mandatory(self):
		return self.__mandatory

	def set_mandatory(self, mandatory):
		self.__mandatory = mandatory
		self.__key_modified["mandatory"] = 1

	def get_layouts(self):
		return self.__layouts

	def set_layouts(self, layouts):
		self.__layouts = layouts
		self.__key_modified["layouts"] = 1

	def get_api_name(self):
		return self.__api_name

	def set_api_name(self, api_name):
		self.__api_name = api_name
		self.__key_modified["api_name"] = 1

	def get_content(self):
		return self.__content

	def set_content(self, content):
		self.__content = content
		self.__key_modified["content"] = 1

	def get_system_mandatory(self):
		return self.__system_mandatory

	def set_system_mandatory(self, system_mandatory):
		self.__system_mandatory = system_mandatory
		self.__key_modified["system_mandatory"] = 1

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

	def get_created_source(self):
		return self.__created_source

	def set_created_source(self, created_source):
		self.__created_source = created_source
		self.__key_modified["created_source"] = 1

	def get_field_read_only(self):
		return self.__field_read_only

	def set_field_read_only(self, field_read_only):
		self.__field_read_only = field_read_only
		self.__key_modified["field_read_only"] = 1

	def get_validation_rule(self):
		return self.__validation_rule

	def set_validation_rule(self, validation_rule):
		self.__validation_rule = validation_rule
		self.__key_modified["validation_rule"] = 1

	def get_read_only(self):
		return self.__read_only

	def set_read_only(self, read_only):
		self.__read_only = read_only
		self.__key_modified["read_only"] = 1

	def get_association_details(self):
		return self.__association_details

	def set_association_details(self, association_details):
		self.__association_details = association_details
		self.__key_modified["association_details"] = 1

	def get_quick_sequence_number(self):
		return self.__quick_sequence_number

	def set_quick_sequence_number(self, quick_sequence_number):
		self.__quick_sequence_number = quick_sequence_number
		self.__key_modified["quick_sequence_number"] = 1

	def get_custom_field(self):
		return self.__custom_field

	def set_custom_field(self, custom_field):
		self.__custom_field = custom_field
		self.__key_modified["custom_field"] = 1

	def get_visible(self):
		return self.__visible

	def set_visible(self, visible):
		self.__visible = visible
		self.__key_modified["visible"] = 1

	def get_length(self):
		return self.__length

	def set_length(self, length):
		self.__length = length
		self.__key_modified["length"] = 1

	def get_decimal_place(self):
		return self.__decimal_place

	def set_decimal_place(self, decimal_place):
		self.__decimal_place = decimal_place
		self.__key_modified["decimal_place"] = 1

	def get_view_type(self):
		return self.__view_type

	def set_view_type(self, view_type):
		self.__view_type = view_type
		self.__key_modified["view_type"] = 1

	def get_pick_list_values(self):
		return self.__pick_list_values

	def set_pick_list_values(self, pick_list_values):
		self.__pick_list_values = pick_list_values
		self.__key_modified["pick_list_values"] = 1

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

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
