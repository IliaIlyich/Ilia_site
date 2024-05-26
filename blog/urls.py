from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts-page"), 
    path("posts/<slug:slug>", views.post_detail, name="detail-page") # "slug" - the name of concept with dynamic segment. The slug is unique 

]
