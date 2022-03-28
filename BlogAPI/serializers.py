from multiprocessing import managers
from pyexpat import model
from Application.models import *
from rest_framework import serializers

'''
[
    {
       user:{

       } 
    }
]
'''

class UserSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','id'] 


class PostSerializers(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializers()
    class Meta:
        model = Post
        fields=['title','post_image','content','category',"id","user"]






class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Profile
        fields = ['user','id']