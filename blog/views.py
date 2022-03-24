from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    # Create your views here.


def contact(request):
    return render(request, 'contact.html', {})

def profile(request):
    return render(request, 'Profile.html', {})

def publications(request):
    return render(request, 'Publications.html', {})

def books(request):
    return render(request, 'books.html', {})

def home(request):
    return render(request, 'index.html', {})
