from django.contrib import admin
from blogs.models import Category, Blogs, Comment, React
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'category_name', 'created_at', 'updated_at')

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','category', 'author', 'blog_image','is_featured', 'status', 'created_at',)
    prepopulated_fields={'slug':('title',)}
    search_fields=('id', 'title', 'category__category_name','author__username')
    list_editable=('status','is_featured')
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment)
admin.site.register(React)