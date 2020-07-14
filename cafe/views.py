from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe:baseball_photo')
    else:
        form = PostForm()
    return render(request, 'cafe:baseball_photo', {'form' : form})
    # profile.photo = request.FILES['photo']

def form(request):
    return render(request, 'cafe/post_form.html')

def detail(request):
    return render(request, 'cafe/post_detail.html')

def photo(request):
    post = Post.objects.all()
    context = {'posts' : post}
    return render(request, 'cafe/photo.html', context)

def movie(request):
    return render(request, 'cafe/movie.html')

def create_photo(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'cafe/create_photo.html', {'form' : form})

def create_post(request):
    return render(request, 'cafe/create_post.html')

def photo_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'cafe/photo_form.html', {'form' : form})

def photo_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post' : post}
    return render(request, 'cafe/photo_detail.html', context)

def howto(request):
    return render(request, 'cafe/howto.html')
