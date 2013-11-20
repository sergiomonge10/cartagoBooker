from django import forms
from main.models import userProfile

class ContactForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Title = forms.CharField(widget=forms.TextInput())
	Comment = forms.CharField(widget=forms.Textarea())

class ProfileForm(forms.ModelForm):
	class Meta:
		model = userProfile
		exclude = ('object_id','user')


		