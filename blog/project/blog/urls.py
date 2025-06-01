from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]