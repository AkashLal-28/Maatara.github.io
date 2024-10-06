from django.db import models

class ContactUs(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

class Newsletter(models.Model):
    sub_email = models.EmailField()
