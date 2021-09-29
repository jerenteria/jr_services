from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postdata):
        email_check=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['l_n']) < 2:
            errors['f_n'] = "First name must be longer than 2 characters"
        if not email_check.match(postdata['email']):
            errors['email'] = "Email must be valid format"
        if len(postdata['pw']) < 8:
            errors['pw'] ="Password must be at least 8 characters long"
        if postdata['pw'] != postdata['conf_pw']:
            errors['conf_pw'] = "Password must match"
        return errors
class User(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    
