from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
"""
  In this senario User with post make one to many relationship
  one user do many posts,But post have only one user
  for migrate the db after doing this typwing this command
   python manage.py makemigrations
   if check database how to work then type in cmd/terminal
    python manage.py sqlmigrate blog 0001(any db reference who created in migration folder)
"""
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
      return self.title
    
