from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):

	def url(self,filename):
		route = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return route

	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to=url)
	phone = models.CharField(max_length=100,blank=True,null=True)
	facebook = models.CharField(max_length=100,blank=True,null=True)
	twitter = models.CharField(max_length=100,blank=True,null=True)
	gplus = models.CharField(max_length=100,blank=True,null=True)
	#other = models.CharField(max_length=100,blank=True,null=True)
	#other2 = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.user.username
		
		