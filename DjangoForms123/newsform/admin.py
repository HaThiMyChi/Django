from django.contrib import admin
from .models import Post, PostLogin

# Register your models here.

admin.site.register(Post)

admin.site.register(PostLogin)