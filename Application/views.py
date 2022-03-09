
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import check_password,make_password
from django.views.generic import View
from .models import Post, Category
from django.contrib.auth.models import User

# Create your views here.
class IndexView(View):
    def get(self, request):
        # if request.user.is_authenticated():
            return render(request, 'index.html')
        # else:
            # return redirect('login')


    def post(self,request):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        email=request.POST['email']
        password2=request.POST['password2']
        if len(firstname)!=0 and len(lastname)!=0 and len(username)!=0 and len(password1)!=0 and len(email)!=0 and len(password2)!=0:
            if not User.objects.filter(username=username).exists():
                if password1 == password2:
                    user = User.objects.create(first_name=firstname,last_name=lastname,username=username,password=make_password(password1),email=email)
                    user.save()
                    return redirect('MainBody')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request,'index.html')
                # user = User.objects.create(username=username, password=password1, email=email, first_name=firstname, last_name=lastname )
                # user.save()
                # print('user created')
            
        
    

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
        if request.user.is_authenticated:
            blog=Post.objects.all()
            context= {
                'post':blog,
            }
            return render(request, 'mainbody.html', context)
        else:
            return redirect('login')


class DetailBlog(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            blog=Post.objects.get(id=id)
            context= {
            'post':blog,
            }
            return render(request, 'detailedblog.html', context)
        else:
            return redirect('login')

class AddBlog(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'addblog.html')
        else:
            return redirect('login')

    def post(request):
        category = Category.objects.all()
        if request.user.is_authenticated:
            if request.method == "POST":
                if request.user.is_authenticated:
                    title = request.POST.get('title')
                    content = request.POST.get()



class Profile(View):
    
    def get(self, request, username):
        if request.user.is_authenticated:
            user=User.objects.get(username=username)
            context={
            'user':user,
        }
            return render(request, 'profile.html',context)
        else:
            return redirect('login')

class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('login')


# class Category(View):
#     def get(self, request):
#         return render(request, 'category.html')


class Signup(View):
    def get(self, request):
        return render(request, 'index.html')




# class DeletePost(DeleteView):
#     model = Post
#     success_url = '/blog/home'
