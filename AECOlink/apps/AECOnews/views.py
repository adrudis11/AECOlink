from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    post = Post(title="Title", body="Text", image="Image");
    post.save(force_insert=True)
    return render(request, 'index.html', { "post" : post })
