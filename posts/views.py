from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from .forms import CustomUserForm, CustomLoginForm, AddPostForm
from .models import Post
# Create your views here.
def index(request):
    return render(request,"posts/index.html",{"name":"srivatsan"})

def user_register(request):
    if request.method=="POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            confpassword = form.cleaned_data['confirm_password']
            if password!=confpassword:
                return redirect("/posts/register/")
            user = User.objects.create_user(username=username,password=password)
            user.save()
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            else:
                return redirect("/posts/")
            return redirect("/posts/home/")

    form = CustomUserForm()
    return render(request,"posts/register.html",{"form":form})

def home(request,id=-1):
    print(request.method)
    if request.user.is_authenticated:
        if request.method=="POST":
            post = Post.objects.get(pk=id)
            post.delete()
            return redirect("/posts/home")
        posts = request.user
        posts = posts.post_set.all()
        return render(request,"posts/home.html",{"posts":posts})
    else:
        return redirect("/posts/register")

def user_logout(request):
    logout(request)
    return redirect("/posts/")

def user_login(request):
    if request.method=="POST":
        form=CustomLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["Username"]
            password=form.cleaned_data["Password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/posts/home/")
            return redirect("/posts/")
    form = CustomLoginForm()
    return render(request,"posts/login.html",{"form":form})


def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = AddPostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                body = form.cleaned_data["body"]
                post = Post()
                post.title = title
                post.body = body
                post.user_id = request.user
                post.save()
                return redirect("/posts/home/")
        form = AddPostForm()
        return render(request,"posts/add_post.html",{"form":form})
    else:
        return redirect("/posts/")

def show_post(request,id):
    post=Post.objects.get(pk=id)
    # created_by=User.objects.get(username=post.user_id)
    return render(request,"posts/show_post.html",{'post':post})

def all_posts(request):
    posts=Post.objects.all()
    return render(request,"posts/all_posts.html",{'posts':posts})

def edit_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            post = Post.objects.get(pk=id)
            title = request.POST['title']
            body = request.POST['body']
            post.title = title
            post.body = body
            post.save()
            return redirect("/posts/show_post/"+str(id))
        post = Post.objects.get(pk=id)
        return render(request,"posts/edit_post.html",{"post":post})
    else:
        return redirect("/posts/home/")