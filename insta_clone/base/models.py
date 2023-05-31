from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    post_category = [
        ("T", "Text"),
        ("I", "Image"),
        ("V", "Video"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=1, choices=post_category,null=True,blank=True)

    text = models.CharField(max_length=500,blank=True,null=True)
    image = models.ImageField(null=True,blank=True)
    post_file = models.FileField(null=True,blank=True)

    class Meta:
        ordering = ["-created"]





