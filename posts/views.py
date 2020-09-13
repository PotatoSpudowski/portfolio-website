from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib import auth

from .models import Post, PostView
from marketing.models import Signup

def index(request):
    queryset = Post.objects.filter(featured=True)
    queryset = Post.objects.order_by('-timestamp')
    
    if request.method == "POST":
        if request.user.is_authenticated:
            auth.logout(request)
        else:
            try:
                email = request.POST["loginemail"]
                password = request.POST["loginpassword"]
                user=auth.authenticate(username=email,password=password)
                if user is not None: 
                    user = User.objects.get(username=email)
                    auth.login(request,user)
            except:
                _ = 0


        # new_signup = Signup()
        # new_signup.email = email
        # new_signup.password = password
        # new_signup.save()

    context = {
        'object_list': queryset
    }

    return render(request, 'index.html', context)

def signup(request):
    queryset = Post.objects.filter(featured=True)
    queryset = Post.objects.order_by('-timestamp')

    context = {
        'object_list': queryset
    }

    try:
        user=User.objects.get(username=request.POST['email'])
        return redirect('index')
    except User.DoesNotExist: # condition for if user doesn't exist and the passwords entered match
        user=User.objects.create_user(username=request.POST['email'],password=request.POST['password'])
        auth.login(request,user)

    return redirect('index')

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def post(request, id):
    post_object = get_object_or_404(Post, pk=id)
    
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post_object)
    
    return render(request, 'detail.html', {'post_object':post_object})