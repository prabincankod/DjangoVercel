from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    message = "hello world from views.py from vercel and hacktoberfest"
    return HttpResponse(message)
