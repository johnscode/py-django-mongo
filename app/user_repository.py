from mongo_utils import get_collection_handle
from .models import User
from bson import ObjectId


class UserRepository:
    def __init__(self):
        self.collection = get_collection_handle('users')

    def create_user(self, user):
        result = self.collection.insert_one(user.to_dict())
        user._id = result.inserted_id
        return user

    def get_user_by_id(self, user_id):
        user_data = self.collection.find_one({'_id': ObjectId(user_id)})
        return User.from_dict(user_data) if user_data else None

    def get_user_by_username(self, username):
        user_data = self.collection.find_one({'username': username})
        return User.from_dict(user_data) if user_data else None

    def update_user(self, user):
        self.collection.update_one(
            {'_id': user._id},
            {'$set': user.to_dict()}
        )

    def delete_user(self, user_id):
        self.collection.delete_one({'_id': ObjectId(user_id)})
