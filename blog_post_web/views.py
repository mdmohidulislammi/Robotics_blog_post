from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogs.models import Category,Blogs
from datetime import date
from blog_post_web.forms import Registration_Form, Login_Form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User



def home(request):
    current_year=date.today().year
    categories=Category.objects.all()
    featured_posts=Blogs.objects.filter(is_featured=True,status=1)
    normal_post=Blogs.objects.filter(is_featured=False,status=1)
    
    context={
        'featured':featured_posts,
        'posts':normal_post,
        'year':current_year,
        'categories':categories
    }
    return render(request,'home_page.html',context)

def posts(request):
    current_year=date.today().year
    categories=Category.objects.all()
    blogs=Blogs.objects.filter(status=1).select_related('author', 'category')
    context={
        'year':current_year,
        'categories':categories,
        'blogs':blogs
    }
    return render(request,'posts.html',context)

# login funtion
def login_page(request):
    current_year = date.today().year
    categories = Category.objects.all()
    if request.method=='POST':
        form=Login_Form(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form=Login_Form()
    context={
        'year':current_year,
        'categories':categories,
        'form':form
    }
    return render(request, 'login.html', context)

def logOut(request):
    logout(request)
    return redirect('home')


# Register funcitonality
def signUp(request):
    current_year=date.today().year
    categories=Category.objects.all()
    if request.method == "POST":
        form = Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = Registration_Form()

    context={
        'form':form,
        'year':current_year,
        'categories':categories
    }

    return render(request, "register.html", context)

