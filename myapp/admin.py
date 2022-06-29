from django.contrib import admin
from .models import Book,MyUser
admin.site.register([Book,MyUser])