from django.db import models


class Post(models.Model):
	date = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	summary = models.TextField()
	category = models.CharField(max_length=100)
	post_data = models.TextField()
	header_image = models.CharField(max_length=100)
