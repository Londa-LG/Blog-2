from django.shortcuts import render
from django.http import HttpResponse


def Dashboard(request):
	return HttpResponse("<h1>admin homepage</h1>")

def Posts(request):
	return HttpResponse("<h1>posts</h1>")

def Edit_Post(request):
	return HttpResponse("<h1>edit post</h1>")

def Users(request):
	return HttpResponse("<h1>users</h1>")

def Edit_User(request):
	return HttpResponse("<h1>edit user</h1>")
