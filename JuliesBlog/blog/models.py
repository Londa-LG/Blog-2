from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
	summary = models.TextField()
	post_data = models.TextField()
	slug = models.TextField(max_length=150, blank=True)
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=100)
	header_image = models.CharField(max_length=100)

	def save(self, *args, **kwargs):
		self.slug = slugify(f"{self.title}")
		super().save(*args,*kwargs)

	def get_absolute_url(self):
		return reverse('Blog:post', kwargs={'post': self.slug})
