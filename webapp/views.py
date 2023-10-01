from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    message = "Making a Standard Template for vercel deployment"
    return HttpResponse(message)
