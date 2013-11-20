from django import forms
from book.models import Book

class addBookForm(forms.ModelForm):    
    class Meta:
        model = Book
        exclude = ('object_id','user','thumbnail')