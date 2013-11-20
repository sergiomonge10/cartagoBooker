from django.contrib import admin
from book.models import Book, Gender

admin.site.register(Book)
admin.site.register(Gender)