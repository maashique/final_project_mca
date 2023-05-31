from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200,null=True)
    prof = models.ImageField(null=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)

class Products(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    img = models.FileField(null=True)
    pRev = models.IntegerField(null=True,default=0)
    Rat = models.IntegerField(null=True,default=0)


class Requirements(models.Model):
    desc = models.CharField(max_length=200)
    date = models.DateField(null=True, auto_now=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)


class Response(models.Model):
    url1 = models.CharField(max_length=20, null=True)
    desc1 = models.CharField(max_length=200, null=True)
    rate1 = models.CharField(max_length=20, null=True)
    img1 = models.URLField(null=True)
    url2 = models.CharField(max_length=20, null=True)
    desc2 = models.CharField(max_length=200, null=True)
    rate2 = models.CharField(max_length=20, null=True)
    img2 = models.URLField(null=True)
    url3 = models.CharField(max_length=20, null=True)
    desc3 = models.CharField(max_length=200, null=True)
    rate3 = models.CharField(max_length=20, null=True)
    img3 = models.URLField(null=True)
    requirements = models.ForeignKey(Requirements, on_delete=models.CASCADE)


class Feedback(models.Model):
    feedback = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)


class Wishlist(models.Model):
    site = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    newRate = models.CharField(max_length=20, null=True)
    offer = models.CharField(max_length=20, null=True)



class Reviews(models.Model):
    review = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)