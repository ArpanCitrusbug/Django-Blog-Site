from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=20, null=False)



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('MainBody')


class Post(models.Model):
    title= models.CharField(max_length=60, null=False)
    content=models.TextField(null=False)
    user= models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    category= models.ForeignKey( Category, null=False, on_delete=models.CASCADE)
    publish_date= models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to="post/image", null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.user)
    
    def get_absolute_url(self):
        return reverse('Detailed_Blog', kwargs={"id":(self.id)})

    class Meta:
        ordering = ['-publish_date']



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name
