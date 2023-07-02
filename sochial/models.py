from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.




class Post(models.Model):
    user = models.CharField(max_length=25)
    description = models.TextField(max_length=30000)
    image = models.ImageField(null=True, blank=True,upload_to='sochial')
    create_date = models.DateTimeField(default=timezone.now)
    likes= models.ManyToManyField(User,related_name = 'like_user')
    def __str__(self):
        return self.user


    
    
    
class Comment(models.Model):
        post = models.ForeignKey(Post,related_name='post_comment', on_delete=models.CASCADE)
        user = models.ForeignKey(User,related_name='post_user' ,on_delete=models.CASCADE)
        content = models.TextField(max_length=16000)
        timestamp = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return str(self.post)