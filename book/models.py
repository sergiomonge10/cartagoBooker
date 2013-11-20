from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):

	def url(self,filename):
		route = "MultimediaData/Books/%s"%(filename)
		return route

	def url_thumbnail(self,filename):
		route = "MultimediaData/Thumbnails/%s"%(filename)
		return route

	book =  models.FileField(upload_to=url)
	user =  models.ForeignKey(User)
	title = models.CharField(max_length=100)
	thumbnail = models.ImageField(upload_to=url_thumbnail,blank=True,null=True)
	year = models.IntegerField()
	gender = models.OneToOneField('Gender')

	def __unicode__(self):
		return self.user.username

class Gender(models.Model):
	name = models.CharField(max_length=100)
	enable = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name
		
		
