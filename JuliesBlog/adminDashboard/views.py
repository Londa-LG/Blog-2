from blog.models import Post
from .forms import New_Post_Form
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url="/admin/login/")
def Logout(request):
    logout(request)
    return redirect("Dashboard:admin-login")

def Posts(request):
	posts = Post.objects.all()

	context = {
		"posts": posts,
	}
	return render(request,"adminposts.html",context)

def Edit_Post(request,post):
	post_obj = get_object_or_404(Post, slug=post)

	if request.method == "POST":
		form = New_Post_Form(request.POST)
		if form.is_valid():
			changes = New_Post_Form(request.POST, instance=post_obj)
			changes.save()
			return redirect("Dashboard:admin-posts")
	else:
		post_form = New_Post_Form(instance=post_obj)

	context={
		"form": post_form
	}
	return render(request,"editpost.html",context)

def Create_Post(request):
	if request.method == "POST":
		form = New_Post_Form(request.POST)
		if form.is_valid():
			newPost = New_Post_Form(request.POST)
			newPost.save()
			return redirect("Dashboard:admin-posts")
	else:
		post_form = New_Post_Form()

	context = {
		'form': post_form
	}
	return render(request,'create.html',context)

