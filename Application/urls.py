from unicodedata import name
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from Application.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('login', LogIn.as_view(), name="login"),
    path('home', MainBody.as_view(), name="MainBody"),
    path('detail/<int:id>', DetailBlog.as_view(), name="Detailed Blog"),
    path('addblog', AddBlog.as_view(), name="Add Blog"),
    path('profile/<str:username>', Profile.as_view(), name="Profile"),
    path('logout', Logout.as_view(), name="Logout"),
    path('signup', Signup.as_view(), name="Signup"),
    path('blog/<int:id>/delete', DeletePost.as_view(), name="deleteblog"),
    path('loggedinProf/<str:username>', LoggedInUser.as_view(), name="LoggedInUser"),
    path('validateemail', csrf_exempt(EmailValidation.as_view()), name="emailvalidate"),
]