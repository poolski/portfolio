from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from tagging.fields import TagField
from tagging.models import Tag
from autoslug import AutoSlugField

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=512)
	description = models.TextField()
	slug = AutoSlugField(max_length=50, unique=True, populate_from='title')
	dateModified = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Discipline(models.Model):
	title = models.CharField(max_length=512)
	description = models.TextField()
	slug = AutoSlugField(max_length=50, unique=True, populate_from='title')

	def __unicode__(self):
		return self.title

class Image(models.Model):
	title = models.CharField(max_length=512)
	description = models.TextField()
	imageFile = ImageWithThumbsField(upload_to='images', sizes=(200,200))
	stub = models.CharField(max_length=50)
	dateModified = models.DateTimeField(auto_now_add=True)
	tags = TagField()
	album = models.ForeignKey(Album)
	discipline = models.ForeignKey(Discipline)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='title')

	def get_tags(self):
		return Tag.objects.get_for_object(self) 

	def __unicode__(self):
		return self.title

