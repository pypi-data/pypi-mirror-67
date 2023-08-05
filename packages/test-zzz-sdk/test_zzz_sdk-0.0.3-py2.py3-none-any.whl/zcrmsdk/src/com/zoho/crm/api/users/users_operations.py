from ..param import Param
from ..param_map import ParameterMap
from ..util import APIResponse
from ..util import CommonAPIHandler

class UsersOperations(object):
	def __init__(self):
		pass


	def get_users(self, param_instance):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/users"
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		handler_instance.param=param_instance
		from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, "application/json")

	def create_users(self, request):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/users"
		handler_instance.api_path=api_path
		handler_instance.http_method="POST"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, "application/json")

	def update_users(self, request):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/users"
		handler_instance.api_path=api_path
		handler_instance.http_method="PUT"
		handler_instance.content_type="application/json"
		handler_instance.request=request
		from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, "application/json")

	def get_user(self, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/users/"
		api_path = api_path + id.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="GET"
		from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, "application/json")

	def delete_user(self, id):
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + "/crm/v2/users/"
		api_path = api_path + id.__str__()
		handler_instance.api_path=api_path
		handler_instance.http_method="DELETE"
		from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, "application/json")

class GetUsersParam(object):
	type = Param("type")


