from unicodedata import name
from django.urls import path
from Application.views import AddBlog, DetailBlog, IndexView, LogIn, MainBody, Profile

from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="Home"),
    path('login', LogIn.as_view(), name="Login"),
    path('home', MainBody.as_view(), name="Main Body"),
    path('detail/<int:id>',DetailBlog.as_view(), name="Detailed Blog"),
    path('addblog', AddBlog.as_view(), name="Add Blog"),
    path('profile/<str:username>', Profile.as_view(), name="Profile")
]
