from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.

def manage_view(request):
    if request.method == 'GET':
        return HttpResponse("'\hello', '\\now_date', '\goodby")

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')

def now_date_view(request):
    if request.method == 'GET':
        now_date = datetime.now()
        return HttpResponse(f"{now_date}")

def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user')