from django import forms
from blog.models import Post

class New_Post_Form(forms.ModelForm):
	class Meta:
		model= Post
		fields = [
			'header_image',
			'title',
			'author',
			'summary',
			'post_data',
			'category'
		]
