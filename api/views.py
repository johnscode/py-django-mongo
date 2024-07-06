from django.http import JsonResponse


def status_check(request):
    return JsonResponse({"message": "Up and running"})

