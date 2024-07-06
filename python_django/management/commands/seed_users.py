from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from pymongo import MongoClient
from bson import ObjectId
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with some default users'

    def handle(self, *args, **options):
        client = MongoClient(settings.MONGO_CLIENT.address[0])
        db = client[settings.MONGO_DB.name]
        users_collection = db['users']

        # Define default users
        default_users = [
            {
                '_id': ObjectId(),
                'username': 'admin',
                'email': 'god@johnscode.com',
                'password': make_password('notreallygod'),
                'is_admin': True
            },
            {
                '_id': ObjectId(),
                'username': 'john',
                'email': 'dev@johnscode.com',
                'password': make_password('devpassword'),
                'is_admin': False
            },
        ]

        # Check if users already exist
        for user in default_users:
            existing_user = users_collection.find_one({'username': user['username']})
            if existing_user:
                self.stdout.write(self.style.WARNING(f"User '{user['username']}' already exists. Skipping."))
            else:
                users_collection.insert_one(user)
                self.stdout.write(self.style.SUCCESS(f"Successfully created user '{user['username']}'"))

        # Create index on username and email
        users_collection.create_index('username', unique=True)
        users_collection.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with default users'))