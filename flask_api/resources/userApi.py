from flask import Response, request
from database.model import User
from flask_restful import  Resource
from mongoengine import errors as mongo_errors
from pymongo import errors as pymongo_errors


class UserListApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json",status=200)

    def post(self):
        try:
            body = request.get_json()
            new_user = User(**body).save()
            id_usr = new_user.id
        except mongo_errors.ValidationError as e:
            return {"error":str(e)}, 404
        except mongo_errors.FieldDoesNotExist as e:
            return {"error":str(e)},404
        except pymongo_errors.DuplicateKeyError as e:
            return {"message":"User exist"},404
        except mongo_errors.NotUniqueError as e:
            return {"message":"User exist"},404
        return {"id":str(id_usr)}, 201


class UserApi(Resource):

    def get(self, id):
        try:
            user = User.objects().get(id=id).to_json()
        except mongo_errors.ValidationError:
            return 404
        except mongo_errors.DoesNotExist as e:
            return {"error":str(e)}, 404

        return Response(user, mimetype="application/json", status=200)

    def put(self, id):
        try:
            body = request.get_json()
            User.objects().get(id=id).update(**body)
        except mongo_errors.ValidationError:
            return 403
        except mongo_errors.DoesNotExist as e:
            return {"error": str(e)}, 403
        return 201

    def delete(self, id):
        User.objects().get(id=id).delete()
        return 204
