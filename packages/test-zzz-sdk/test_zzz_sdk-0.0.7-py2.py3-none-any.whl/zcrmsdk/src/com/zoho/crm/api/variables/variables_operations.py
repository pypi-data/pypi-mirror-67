from ..param import Param
from ..param_map import ParameterMap
from ..util import APIResponse
from ..util import CommonAPIHandler

class VariablesOperations(object):
	def __init__(self):
		pass


	def get_variables(self, param_instance, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables"
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		handler_instance.param=param_instance
		from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, "application/json")

	def create_variables(self, request):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables"
		handler_instance.api_path=api_path
		handler_instance.http_method="POST"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

	def update_variables(self, request):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables"
		handler_instance.api_path=api_path
		handler_instance.http_method="PUT"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

	def delete_variables(self, param_instance):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables"
		handler_instance.api_path=api_path
		handler_instance.http_method="DELETE"
		handler_instance.param=param_instance
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

	def get_variable_by_id(self, param_instance, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + id.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		handler_instance.param=param_instance
		from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, "application/json")

	def get_variable_by_group_api_name(self, param_instance, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + id.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		handler_instance.param=param_instance
		from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, "application/json")

	def update_variable_by_id(self, request, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + id.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="PUT"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

	def delete_variable(self, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + id.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="DELETE"
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

	def get_variable_for_group_id(self, param_instance, api_name):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + api_name.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		handler_instance.param=param_instance
		from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, "application/json")

	def get_variable_for_group_api_name(self, param_instance, api_name):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + api_name.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		handler_instance.param=param_instance
		from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, "application/json")

	def update_variable_by_api_name(self, request, api_name):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + api_name.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="PUT"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

	def delete_variable_by_api_name(self, api_name):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/variables/"
		api_path = api_path + api_name.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="DELETE"
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")

class GetVariablesParam(object):
	group = Param("group")




class DeleteVariablesParam(object):
	ids = Param("ids")




class GetVariableByIDParam(object):
	group = Param("group")




class GetVariableByGroupAPINameParam(object):
	group = Param("group")




class GetVariableForGroupIDParam(object):
	group = Param("group")




class GetVariableForGroupAPINameParam(object):
	group = Param("group")


