from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'Kashif',
        'title' :'Programming',
        'content':'Now a days! Coding work is done very fast and solve our problem.so we try to avoid the all problem that we not fixed.so computer programming is basically telling the computer what to do',
        'date_posted':'March 17 2020'
    },
    {
        'author':'Haider',
        'title' :'Prophet Muhammad',
        'content':'Prophet Muhammad(saw) says! I am the city of knowledge Ali(as) is his Gate come for gate let me more! ',
        'date_posted':'March 19 2020'
    },
    
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

