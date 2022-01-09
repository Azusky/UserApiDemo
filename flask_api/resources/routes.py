from .userApi import UserListApi, UserApi

def init_routes(api):
    api.add_resource(UserListApi,'/api/user')
    api.add_resource(UserApi,'/api/user/<id>')
