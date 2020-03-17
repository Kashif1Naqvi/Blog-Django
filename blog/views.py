from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'Kashif',
        'title' :'Blog post 1',
        'content':'Blog post content',
        'date_posted':'March 17 2020'
    },
    {
        'author':'Hassan',
        'title' :'Blog post 2',
        'content':'Blog post contents ',
        'date_posted':'March 18 2020'
    },
    
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

