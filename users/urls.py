from django.urls import path, include
from users.views import user_profile, manager_dashboard, create_post, delete_post, update_post,add_user,update_user, delete_user

urlpatterns = [
     path('user/<int:id>/', user_profile,name='user_profile'),
     path('manager/',manager_dashboard, name='manager_dashboard' ),
     path('create-post/', create_post, name='create_post'),
     path('delete-post/<int:id>', delete_post, name='delete_post'),
     path('update-post/<int:id>', update_post, name='update_post'),
     # CRUD in user by manager
     path('add_user/', add_user, name="add_user"),
     path('update-user/<int:id>/', update_user, name='update_user'),
     path('delete-user/<int:id>/', delete_user, name='delete_user')
]
