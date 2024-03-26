from blog.models import Post
from django.urls import reverse
from .forms import New_Post_Form
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm	
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("Status/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    content = {'form': form}
    return render(request, 'login.html', content)

def Logout(request):
    logout(request)
    messages.info(request,'Logout successful')
    return redirect('admin-dashboard')

def Dashboard(request):
	return HttpResponse("<h1>admin homepage</h1>")

def Posts(request):
	posts = Post.objects.all()

	context = {
		"posts": posts,
	}
	return render(request,"adminposts.html",context)

def Edit_Post(request,post):
	post_obj = get_object_or_404(Post, slug=post)
	post_form = New_Post_Form(instance=post_obj)

	context={
		"form": post_form
	}
	return render(request,"editpost.html",context)

def Create_Post(request):
	post_form = New_Post_Form(request.POST or None)

	context = {
		'form': post_form
	}
	return render(request,'create.html',context)

