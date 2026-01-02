from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from blogs.models import Category, Blogs,Comment, React
from datetime import date
from blogs.forms import Add_post_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import User_Creation

@login_required(login_url="login_page")
def user_profile(request, id):
    current_year = date.today().year
    categories = Category.objects.all()
    if request.user.is_authenticated:
        user_id = request.user.id

    blogs = Blogs.objects.filter(status=1, author=request.user).select_related(
        "category"
    )
    context = {"year": current_year, "categories": categories, "blogs": blogs}
    return render(request, "users_dashboard/profile.html", context)


@login_required(login_url="login_page")
def manager_dashboard(request):
    current_year = date.today().year
    categories = Category.objects.all()
    id = request.user.id
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_staff:
        messages.error(request, "You are not an admin")
        return redirect("user_profile", id)
    blogs = Blogs.objects.filter(status=1).select_related("author", "category")
    users = User.objects.all()
    context = {
        "year": current_year,
        "categories": categories,
        "blogs": blogs,
        "users": users,
    }
    return render(request, "users_dashboard/manage_dashboard.html", context)

def add_user(request):
    current_year = date.today().year
    categories = Category.objects.all()
    form=User_Creation()
    if request.method=='POST':
        form=User_Creation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard')
        else:
            messages.error(request,"Form is not valid")
            return redirect('manager_dashboard')
    
    context={
        'year':current_year,
        'categories':categories,
        'form':form
    }
    return render(request, "users_dashboard/new_user.html", context)


def create_post(request):
    current_year = date.today().year
    categories = Category.objects.all()
    if request.method == "POST":
        form = Add_post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)
            post.save()
            return redirect("posts")
        else:
            id=request.user.id
            messages.error(request, "Post is not valid. Please try again...")
            return redirect("user_profile", id)
    else:
        form = Add_post_form()

    context = {"year": current_year, "categories": categories, "form": form}

    return render(request, "addPostForm.html", context)


def delete_post(request, id):
    blog=Blogs.objects.select_related('author', 'category').filter(id=id, status=1)
    blog.delete()
    messages.success(request,'Post deleted Successfully')
    return redirect('user_profile', request.user.id)

def update_post(request, id):
     current_year = date.today().year 
     categories = Category.objects.all() 
     post = get_object_or_404(Blogs, id=id) 
     if request.method == "POST": 
        form = Add_post_form(request.POST, request.FILES, instance=post) 
        if form.is_valid(): 
            updated_post = form.save(commit=False) 
            updated_post.author = request.user # keep author consistent 
            title = form.cleaned_data['title'] 
            updated_post.slug = slugify(title) # regenerate slug if title changes 
            updated_post.save() 
            messages.success(request, "Post updated successfully!") 
            return redirect("posts") 
        else: 
         messages.error(request, "Update failed. Please check the form and try again.") 
         return redirect("update_post", id=request.post.id) 
     else: 
        form = Add_post_form(instance=post) 
     context = { "year": current_year, "categories": categories, "form": form, "post": post, } 
     return render(request, "blogs/update_post.html", context)



@login_required(login_url="login_page")
def update_user(request, id):
    current_year = date.today().year
    categories = Category.objects.all()
    user_obj = get_object_or_404(User, id=id)

    if request.method == "POST":
        form = User_Creation(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect("manager_dashboard")
        else:
            messages.error(request, "Update failed. Please check the form and try again.")
            return redirect('manager_dashboard')
    else:
        form = User_Creation(instance=user_obj)

    context = {
        "year": current_year,
        "categories": categories,
        "form": form,
        "user_obj": user_obj,
    }
    return render(request, "users_dashboard/new_user.html", context)


@login_required(login_url="login_page")
def delete_user(request, id):
    user_obj = get_object_or_404(User, id=id)
    if request.user.is_staff:   # only admins can delete
        user_obj.delete()
        messages.success(request, "User deleted successfully!")
        return redirect("manager_dashboard")
    else:
        messages.error(request, "You do not have permission to delete users.")
        return redirect("user_profile", request.user.id)



