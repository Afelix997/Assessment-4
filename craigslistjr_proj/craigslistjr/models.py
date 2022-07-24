from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100, blank = False)

class Post(models.Model):
    title=models.CharField(max_length=200, blank = False)
    description=models.CharField(max_length=200, blank = False)
    posted_by=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
