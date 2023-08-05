from ..util import APIResponse
from ..util import CommonAPIHandler

class ModulesOperations(object):
	def __init__(self):
		pass


	def get_modules(self):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/modules"
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, "application/json")

	def get_module(self, api_name):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/modules/"
		api_path = api_path + api_name.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, "application/json")

	def update_module(self, request, api_name):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/settings/modules/"
		api_path = api_path + api_name.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="PUT"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_wrapper import ActionWrapper
		return handler_instance.api_call(ActionWrapper.__module__, "application/json")
