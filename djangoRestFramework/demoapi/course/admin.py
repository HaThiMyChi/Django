# from django.apps import AppConfig
# #
# #
# # class OrderConfig(AppConfig
from django.contrib import admin
from .models import Course

admin.site.register(Course)