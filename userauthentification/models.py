from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from post.models import Post


# uploading user files to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now= True)
    otp = models.SmallIntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profile_pciture", null=True, default="default.png")
    favourite = models.ManyToManyField(Post, blank=True)
    
    # Theme 
    color_choice = [(252,'purple'),(52,'yellow'),(352,'red'),(152,'green'),(202,'blue')]
    color = models.IntegerField(choices=color_choice,default=252)

    bg_choice = [('bg1','Light'),('bg2','Dim'),('bg3','Dark')]
    bg = models.CharField(max_length=5,choices=bg_choice,default='bg1')

    font_choice = [('f1','Size_1'),('f2','Size_2'),('f3','Size_3'),('f4','Size_4'),('f4','Size_5')]
    font_size = models.CharField(max_length=7,choices=font_choice,default='f2')
    
    # def __str__(self):
    #     return User.username



