from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class LogIn(View):
    def get(self, request):
        return render(request, 'login.html')

class MainBody(View):
    def get(self, request):
        post=Post.objects.all()
        #sending all the blogs with all function
        context= {
            'post':post,
        }
        #this dictionary will send all the data to template
        return render(request, 'mainbody.html',context)


class DetailBlog(View):
    def get(self, request, id):
        blog=Post.objects.get(id=id)
        context= {
            'post':blog,
        }
        return render(request, 'detailedblog.html', context)


class AddBlog(View):
    def get(self, request):
        return render(request, 'addblog.html')

    def post(self,request):
        return render(request, 'addblog.html')


class Profile(View):
    def get(self, request, username):
        user=User.objects.get(username=username)
        context={
            'user':user,
        }
        return render(request, 'profile.html',context)

