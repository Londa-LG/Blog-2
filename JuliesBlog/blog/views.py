from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post

def Blog_Home(request):
	latest_posts = Post.objects.order_by("-date")[:5]

	context = {
		"latest": latest_posts
	}
	return render(request,'home.html',context)

def Blog_Posts(request):
	post_objs = Post.objects.all()

	context = {
		"posts" : post_objs
	}
	return render(request,'posts.html',context)

def Blog_Post(request,post):
	post_obj = get_object_or_404(Post, slug=post)

	context = {
		'post': post_obj
	}
	return render(request,'post.html',context)
