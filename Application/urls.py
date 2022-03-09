from unicodedata import name
from django.urls import path
from Application.models import Category
from Application.views import * 

from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('login', LogIn.as_view(), name="login"),
    path('home', MainBody.as_view(), name="MainBody"),
    path('detail/<int:id>',DetailBlog.as_view(), name="Detailed Blog"),
    path('addblog', AddBlog.as_view(), name="Add Blog"),
    path('profile/<str:username>', Profile.as_view(), name="Profile"),
    path('logout', Logout.as_view(), name="Logout"),
    path('signup',Signup.as_view(), name="Signup")
    # path('category', Category.as_view(), name="Category")
    # path('blog/<int:pk>/delete',DeletePost.as_view(), name= "deleteblog")
]