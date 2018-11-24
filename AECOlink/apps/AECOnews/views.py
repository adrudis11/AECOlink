from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    post = Post.objects.get(title="Title")
    return render(request, 'index.html', { "post" : post })
