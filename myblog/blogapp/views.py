from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def community(request):
    return render(request, 'blogapp/community.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'blogapp/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'blog': blog_detail})