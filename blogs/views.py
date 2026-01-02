from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from blogs.models import Category, Blogs,Comment, React
from datetime import date
from blogs.forms import Add_post_form, CommentForm, ReactForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# show posts by category
def posts_by_category(request,category_id):
    current_year=date.today().year
    categories=Category.objects.all()
    blogs=Blogs.objects.filter(status=1,category=category_id).select_related('author', 'category')
    context={
        'year':current_year,
        'categories':categories,
        'blogs':blogs
    }
    return render(request, 'category.html',context)

# View single post
def post_detail(request,id):
    current_year = date.today().year
    categories = Category.objects.all()
    
    blog = get_object_or_404(Blogs.objects.select_related('author', 'category'),id=id, status=1)
    # For comment, reacts
    blog_reacts_comment = Blogs.objects.select_related('author', 'category').prefetch_related('comment_set', 'react_set').get(id=id, status=1) 
    comments=blog_reacts_comment.comment_set.all()
    reacts=blog_reacts_comment.react_set.all()
    comment_form=CommentForm()
    context = {
        'year': current_year,
        'categories': categories,
        'post': blog,  # pass as 'post' 
        'comments':comments,
        'reacts':reacts,
        'comment_form':CommentForm
    }
    return render(request, 'single_post.html',context)



@login_required(login_url="login_page")
def add_comment(request, id):
    blog = get_object_or_404(Blogs, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, "Comment added successfully!")
    return redirect("post_detail", id=id)


@login_required(login_url="login_page")
def react_to_post(request, id):
    blog = get_object_or_404(Blogs, id=id)
    react, created = React.objects.get_or_create(user=request.user, blog=blog)

    if not created:
        react.delete()  # toggle off
    else:
        react.reacts = True
        react.save()

    return redirect("post_detail", id=id)



# Search functionality
def searchBlogs(request):
    current_year = date.today().year
    categories = Category.objects.all()
    keyword = request.GET.get('keyword')

    blogs = Blogs.objects.none()

    if keyword:
        blogs = Blogs.objects.select_related('author', 'category').filter(
            Q(title__icontains=keyword) |
            Q(author__username__icontains=keyword) |
            Q(category__category_name__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status=1
        )
        if not blogs.exists():
            messages.warning(request, 'No data found ...')
    else:
        messages.error(request, 'Your keyword may be wrong , try again...')

    context = {
        'year': current_year,
        'categories': categories,
        'blogs': blogs,
    }
    return render(request, 'posts.html', context)

