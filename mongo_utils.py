from django.conf import settings

def get_db_handle():
    client = settings.MONGO_CLIENT
    db_handle = settings.MONGO_DB
    return client, db_handle

def get_collection_handle(collection_name):
    _, db_handle = get_db_handle()
    return db_handle[collection_name]
