from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.home_layout, name="home"),
    path('post/', views.post_list, name="postlist"),
    path('post/<int:post_id>/', views.post_detail, name="detailpost")
]