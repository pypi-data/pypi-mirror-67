from ..customview import CustomView
from ..profile import Profile
from ..users import User
from ..util import Model


class Module(Model):
	def __init__(self):
		self.__id = None
		self.__api_name = None
		self.__module_name = None
		self.__convertable = None
		self.__editable = None
		self.__deletable = None
		self.__web_link = None
		self.__singular_label = None
		self.__modified_time = None
		self.__viewable = None
		self.__api_supported = None
		self.__createable = None
		self.__plural_label = None
		self.__generated_type = None
		self.__modified_by = None
		self.__global_search_supported = None
		self.__presence_sub_menu = None
		self.__triggers_supported = None
		self.__feeds_required = None
		self.__filter_supported = None
		self.__scoring_supported = None
		self.__webform_supported = None
		self.__kanban_view = None
		self.__kanban_view_supported = None
		self.__show_as_tab = None
		self.__filter_status = None
		self.__quick_create = None
		self.__emailtemplate_support = None
		self.__inventory_template_supported = None
		self.__description = None
		self.__display_field = None
		self.__visibility = None
		self.__business_card_field_limit = None
		self.__per_page = None
		self.__sequence_number = None
		self.__profiles = None
		self.__custom_view = None
		self.__related_list_properties = None
		self.__properties = None
		self.__search_layout_fields = None
		self.__parent_module = None
		self.__territory = None
		self.__arguments = None
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

	def get_module_name(self):
		return self.__module_name

	def set_module_name(self, module_name):
		self.__module_name = module_name
		self.__key_modified["module_name"] = 1

	def get_convertable(self):
		return self.__convertable

	def set_convertable(self, convertable):
		self.__convertable = convertable
		self.__key_modified["convertable"] = 1

	def get_editable(self):
		return self.__editable

	def set_editable(self, editable):
		self.__editable = editable
		self.__key_modified["editable"] = 1

	def get_deletable(self):
		return self.__deletable

	def set_deletable(self, deletable):
		self.__deletable = deletable
		self.__key_modified["deletable"] = 1

	def get_web_link(self):
		return self.__web_link

	def set_web_link(self, web_link):
		self.__web_link = web_link
		self.__key_modified["web_link"] = 1

	def get_singular_label(self):
		return self.__singular_label

	def set_singular_label(self, singular_label):
		self.__singular_label = singular_label
		self.__key_modified["singular_label"] = 1

	def get_modified_time(self):
		return self.__modified_time

	def set_modified_time(self, modified_time):
		self.__modified_time = modified_time
		self.__key_modified["modified_time"] = 1

	def get_viewable(self):
		return self.__viewable

	def set_viewable(self, viewable):
		self.__viewable = viewable
		self.__key_modified["viewable"] = 1

	def get_api_supported(self):
		return self.__api_supported

	def set_api_supported(self, api_supported):
		self.__api_supported = api_supported
		self.__key_modified["api_supported"] = 1

	def get_createable(self):
		return self.__createable

	def set_createable(self, createable):
		self.__createable = createable
		self.__key_modified["createable"] = 1

	def get_plural_label(self):
		return self.__plural_label

	def set_plural_label(self, plural_label):
		self.__plural_label = plural_label
		self.__key_modified["plural_label"] = 1

	def get_generated_type(self):
		return self.__generated_type

	def set_generated_type(self, generated_type):
		self.__generated_type = generated_type
		self.__key_modified["generated_type"] = 1

	def get_modified_by(self):
		return self.__modified_by

	def set_modified_by(self, modified_by):
		self.__modified_by = modified_by
		self.__key_modified["modified_by"] = 1

	def get_global_search_supported(self):
		return self.__global_search_supported

	def set_global_search_supported(self, global_search_supported):
		self.__global_search_supported = global_search_supported
		self.__key_modified["global_search_supported"] = 1

	def get_presence_sub_menu(self):
		return self.__presence_sub_menu

	def set_presence_sub_menu(self, presence_sub_menu):
		self.__presence_sub_menu = presence_sub_menu
		self.__key_modified["presence_sub_menu"] = 1

	def get_triggers_supported(self):
		return self.__triggers_supported

	def set_triggers_supported(self, triggers_supported):
		self.__triggers_supported = triggers_supported
		self.__key_modified["triggers_supported"] = 1

	def get_feeds_required(self):
		return self.__feeds_required

	def set_feeds_required(self, feeds_required):
		self.__feeds_required = feeds_required
		self.__key_modified["feeds_required"] = 1

	def get_filter_supported(self):
		return self.__filter_supported

	def set_filter_supported(self, filter_supported):
		self.__filter_supported = filter_supported
		self.__key_modified["filter_supported"] = 1

	def get_scoring_supported(self):
		return self.__scoring_supported

	def set_scoring_supported(self, scoring_supported):
		self.__scoring_supported = scoring_supported
		self.__key_modified["scoring_supported"] = 1

	def get_webform_supported(self):
		return self.__webform_supported

	def set_webform_supported(self, webform_supported):
		self.__webform_supported = webform_supported
		self.__key_modified["webform_supported"] = 1

	def get_kanban_view(self):
		return self.__kanban_view

	def set_kanban_view(self, kanban_view):
		self.__kanban_view = kanban_view
		self.__key_modified["kanban_view"] = 1

	def get_kanban_view_supported(self):
		return self.__kanban_view_supported

	def set_kanban_view_supported(self, kanban_view_supported):
		self.__kanban_view_supported = kanban_view_supported
		self.__key_modified["kanban_view_supported"] = 1

	def get_show_as_tab(self):
		return self.__show_as_tab

	def set_show_as_tab(self, show_as_tab):
		self.__show_as_tab = show_as_tab
		self.__key_modified["show_as_tab"] = 1

	def get_filter_status(self):
		return self.__filter_status

	def set_filter_status(self, filter_status):
		self.__filter_status = filter_status
		self.__key_modified["filter_status"] = 1

	def get_quick_create(self):
		return self.__quick_create

	def set_quick_create(self, quick_create):
		self.__quick_create = quick_create
		self.__key_modified["quick_create"] = 1

	def get_emailtemplate_support(self):
		return self.__emailtemplate_support

	def set_emailtemplate_support(self, emailtemplate_support):
		self.__emailtemplate_support = emailtemplate_support
		self.__key_modified["emailTemplate_support"] = 1

	def get_inventory_template_supported(self):
		return self.__inventory_template_supported

	def set_inventory_template_supported(self, inventory_template_supported):
		self.__inventory_template_supported = inventory_template_supported
		self.__key_modified["inventory_template_supported"] = 1

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description
		self.__key_modified["description"] = 1

	def get_display_field(self):
		return self.__display_field

	def set_display_field(self, display_field):
		self.__display_field = display_field
		self.__key_modified["display_field"] = 1

	def get_visibility(self):
		return self.__visibility

	def set_visibility(self, visibility):
		self.__visibility = visibility
		self.__key_modified["visibility"] = 1

	def get_business_card_field_limit(self):
		return self.__business_card_field_limit

	def set_business_card_field_limit(self, business_card_field_limit):
		self.__business_card_field_limit = business_card_field_limit
		self.__key_modified["business_card_field_limit"] = 1

	def get_per_page(self):
		return self.__per_page

	def set_per_page(self, per_page):
		self.__per_page = per_page
		self.__key_modified["per_page"] = 1

	def get_sequence_number(self):
		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		self.__sequence_number = sequence_number
		self.__key_modified["sequence_number"] = 1

	def get_profiles(self):
		return self.__profiles

	def set_profiles(self, profiles):
		self.__profiles = profiles
		self.__key_modified["profiles"] = 1

	def get_custom_view(self):
		return self.__custom_view

	def set_custom_view(self, custom_view):
		self.__custom_view = custom_view
		self.__key_modified["custom_view"] = 1

	def get_related_list_properties(self):
		return self.__related_list_properties

	def set_related_list_properties(self, related_list_properties):
		self.__related_list_properties = related_list_properties
		self.__key_modified["related_list_properties"] = 1

	def get_properties(self):
		return self.__properties

	def set_properties(self, properties):
		self.__properties = properties
		self.__key_modified["$properties"] = 1

	def get_search_layout_fields(self):
		return self.__search_layout_fields

	def set_search_layout_fields(self, search_layout_fields):
		self.__search_layout_fields = search_layout_fields
		self.__key_modified["search_layout_fields"] = 1

	def get_parent_module(self):
		return self.__parent_module

	def set_parent_module(self, parent_module):
		self.__parent_module = parent_module
		self.__key_modified["parent_module"] = 1

	def get_territory(self):
		return self.__territory

	def set_territory(self, territory):
		self.__territory = territory
		self.__key_modified["territory"] = 1

	def get_arguments(self):
		return self.__arguments

	def set_arguments(self, arguments):
		self.__arguments = arguments
		self.__key_modified["arguments"] = 1

	def is_key_modified(self, key):
		return self.__key_modified.get(key)

	def set_key_modified(self, modification, key):
		self.__key_modified[key] = modification
