from django.contrib import admin
from .models import Post, PostLogin, MyUser

# Register your models here.

admin.site.register(Post)

admin.site.register(PostLogin)
admin.site.register(MyUser)