from django.contrib import admin
from .models import Book, category


admin.site.register(Book)
admin.site.register(category)
