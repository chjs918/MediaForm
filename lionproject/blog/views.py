from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import blogForm

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request,'home.html',{'blog' : blog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html' ,{'blog' : blog_detail})

def new(request):
    form = blogForm()
    return render(request,'new.html', {'form':form})

def create(request):
    form = blogForm(request.POST,request.FILES)
    if form.is_valid():
        freshBlog = form.save(commit=False) 
        #빠진 정보를 무시한채 저장하게 되면 pubdate부분이 빈칸으로 저장쌓인다->임시저장
        freshBlog.blog_date = timezone.now()
        freshBlog.save()
        return redirect('detail',freshBlog.id)
    return redirect('home')

def edit(request, blog_id):
    reviseBlog = Blog.objects.get(id = blog_id)
    return render(request, 'edit.html', {'blog' : reviseBlog})


def update(request, blog_id):
    updateBlog = Blog.objects.get(id = blog_id)
    updateBlog.blog_title = request.POST['diaryTitle']
    updateBlog.blog_writer = request.POST['diaryWriter']
    updateBlog.blog_body = request.POST['diaryBody']
    updateBlog.blog_date = timezone.now()
    updateBlog.save()
    return redirect('detail',updateBlog.id)


def delete(request, blog_id):
    deleteBlog =  Blog.objects.get(id = blog_id)
    deleteBlog.delete()
    return redirect('home')