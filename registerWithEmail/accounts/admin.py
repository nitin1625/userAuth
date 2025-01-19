from django.contrib import admin

# Register your models here.

from .models import customUser
admin.site.register(customUser)