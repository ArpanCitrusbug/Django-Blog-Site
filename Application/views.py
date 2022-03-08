import re
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.hashers import check_password,make_password
from django.views.generic import View,DeleteView
from .models import Post, Category
from django.contrib.auth.models import User

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class LogIn(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.get(username=username)
        print(user.password)
        password_check= check_password(password,user.password)
        if password_check:
            auth.login(request, user)
            return redirect('MainBody')
        return render(request, 'login.html')

class MainBody(View):
    def get(self, request):
        # if request.user.is_anticipated():
                
        post=Post.objects.all()
        category=Category.objects.all()
        #sending all the blogs with all function
        context= {
                'post':post,
                'category':category,
            }
            #this dictionary will send all the data to template
        return render(request, 'mainbody.html',context)

        # else:
        return redirect('login')


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

    def post(request):
        category = Category.objects.all()
        if request.user.is_authenticated:
            if request.method == "POST":
                if request.user.is_authenticated:
                    title = request.POST.get('title')
                    content = request.POST.get()



class Profile(View):
    def get(self, request, username):
        user=User.objects.get(username=username)
        context={
            'user':user,
        }
        return render(request, 'profile.html',context)

class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('login')


# class Category(View):
#     def get(self, request):
#         return render(request, 'category.html')


class Signup(View):
    def get(self,request):
        pass


class DeletePost(DeleteView):
    model = Post
    success_url = '/blog/home'
