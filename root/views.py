from django.shortcuts import render
from mongo_utils import get_collection_handle

def home(request):
    collection = get_collection_handle('users')
    count = collection.count_documents({})
    return render(request, 'home.html')

