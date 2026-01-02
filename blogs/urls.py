from django.urls import path
from blogs.views import posts_by_category,post_detail,searchBlogs,add_comment,react_to_post
urlpatterns = [
   path('category/<int:category_id>/',posts_by_category,name='posts_by_category'),
   path('post/<int:id>/',post_detail, name='post_detail'),
   path('search/',searchBlogs, name="searchBlogs"),
   path('post/<int:id>/comment/', add_comment, name='add_comment'),
   path('post/<int:id>/react/', react_to_post, name='react_to_post')
]
