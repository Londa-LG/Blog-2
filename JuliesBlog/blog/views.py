from django.shortcuts import render
from django.http import HttpResponse


def Blog_Home(request):
	return HttpResponse("<h1>Blog home page</h1>")

def Blog_Posts(request):
	return HttpResponse("<h1>Posts view</h1>")

def Blog_Post(request):
	return HttpResponse("<h1>Read Post</h1>")
