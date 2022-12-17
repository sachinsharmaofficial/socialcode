from django.db import models
from django.contrib.auth.models import User
from post.models import Post
import uuid
# Create your models here.


# Importing photos to media
def user_ask_path(instance, filename):
    return 'ask/user_{0}/{1}'.format(instance.user.id, filename)

def user_get_path(instance, filename):
    return 'get/user_{0}/{1}'.format(instance.user.id, filename)

class Ask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Ask")
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=user_ask_path,verbose_name='question')

class GET(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="GET")
    ask = models.ForeignKey(Ask, on_delete=models.CASCADE, related_name="ask")
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=user_get_path,verbose_name="ans")

# class CHAT(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="chat")
#     get = models.ForeignKey(GET, on_delete=models.CASCADE,related_name="get")
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True,null = True )
#     image = models.ImageField(upload_to=user_get_path,verbose_name="comment")
    
