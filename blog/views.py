from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse("<h1>Blog Home page :)</h1>")

def contact(request):
  return HttpResponse("<h1>Blog Contact page :) </h1>")