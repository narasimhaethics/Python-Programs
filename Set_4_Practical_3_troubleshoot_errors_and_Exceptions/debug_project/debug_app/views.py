# debug_app/views.py
from django.http import HttpResponse

def error_view(request):
    # Intentionally raising an exception
    a = 1 / 0
    return HttpResponse("This won't be reached due to the exception")
