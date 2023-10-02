from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    message = "Making a Standard Template for vercel django deployment"
    anotherMessage = "bite my shiny metal ass."
    return HttpResponse(message+anotherMessage)
