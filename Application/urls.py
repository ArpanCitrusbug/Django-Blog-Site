from unicodedata import name
from django.urls import path
from Application.models import Category
from Application.views import AddBlog, DetailBlog, DeletePost, IndexView, LogIn, MainBody, Profile, Logout, Category

from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="Home"),
    path('login', LogIn.as_view(), name="login"),
    path('home', MainBody.as_view(), name="MainBody"),
    path('detail/<int:id>',DetailBlog.as_view(), name="Detailed Blog"),
    path('addblog', AddBlog.as_view(), name="Add Blog"),
    path('profile/<str:username>', Profile.as_view(), name="Profile"),
    path('logout', Logout.as_view(), name="Logout"),
    # path('category', Category.as_view(), name="Category")
    path('blog/<int:pk>/delete',DeletePost.as_view(), name= "deleteblog")
]
