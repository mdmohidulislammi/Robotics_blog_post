
from django.contrib import admin
from django.urls import path, include
from blog_post_web.views import home,posts,login_page, signUp,logOut
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('posts/',posts,name='posts'),
    path('home/',include("blogs.urls")),
    path('', include("users.urls")),
    path('login/', login_page, name='login_page'),
   path('sign-up/', signUp, name="signUp"),
   path('logout/', logOut, name='logOut'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+debug_toolbar_urls()