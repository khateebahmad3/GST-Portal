from django.shortcuts import render, redirect

def index_redirect(request):
	return redirect('/gst/')