from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=500)
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    imagedescription = models.CharField(max_length=500, blank=True)

    image1 = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    imagedescription1 = models.CharField(max_length=500, blank=True)
    post1 = models.CharField(max_length=500, blank=True)

    image2 = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    imagedescription2 = models.CharField(max_length=500, blank=True)
    post2 = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.post


class Homepage(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=700,blank=True)
    image = models.ImageField(upload_to='homepage/%Y/%m/%d', blank=True)

    title1 = models.CharField(max_length=500)
    content1 = models.CharField(max_length=700, blank=True)
    image1 = models.ImageField(upload_to='homepage/%Y/%m/%d', blank=True)
 
    def __str__(self):
        return self.title

class Aboutpage(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=700,blank=True)
    image = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    aboutus = models.TextField(max_length=500, blank=True)
    aboutimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    story = models.TextField(max_length=1500, blank=True)
    storyimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    team = models.TextField(max_length=1500, blank=True)
    teamimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    whyus = models.TextField(max_length=1500, blank=True)
    whyusimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email