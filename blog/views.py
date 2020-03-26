from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #app/model_viewtype.html like blog/post_list.html

    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post