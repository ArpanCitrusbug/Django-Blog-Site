from django.shortcuts import render
from Application.models import *
from rest_framework import serializers
# Create your views here.
class PostSerializers(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields=['title','post_image','content','category',"id","user"]




class UserSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)





class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Profile
        fields = ['user','id']