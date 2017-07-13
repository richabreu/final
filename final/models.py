from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class SourceTag(models.Model):
	name = models.CharField(max_length = 50);
		
	def __unicode__(self):
		return self.name

class SourceUrl(models.Model):
	name = models.CharField(max_length = 50);
	tag = models.ForeignKey(SourceTag)
	url = models.URLField(max_length = 200);
	
	def __unicode__(self):
		return self.url

class User(models.Model):
	name = models.CharField(max_length=128)
	tags = models.ManyToManyField(SourceTag)
	
	def __unicode__(self):
		return self.name