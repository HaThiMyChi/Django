from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length= 255, blank=False, null=False)
	content = models.TextField(max_length=1000, blank=False, null=False)
	time_created = models.DateTimeField(default=timezone.datetime.now())
	
	def __str__(self):
		return self.title
	
class PostLogin(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=255)
	
	def __str__(self):
		return self.title
	
class MyUser(AbstractUser):
	sex_choice = ((0, "Nu"), (1, "Nam"), (2, "Gioi tinh khong xac dinh"))
	age = models.IntegerField(default = 0)
	sex = models.IntegerField(choices=sex_choice, default=0) # default = 0 la chon nu
	address = models.CharField(default='', max_length=255)
	
	