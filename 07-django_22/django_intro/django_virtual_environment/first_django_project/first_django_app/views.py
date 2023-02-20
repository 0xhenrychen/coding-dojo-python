from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return redirect("/blogs")

def index_method(request):
    return HttpResponse("Placeholder to later display a list of all blogs.")

def new_method(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")

def create_method(request):
    return redirect("/")

def show_method(request, number):
    return HttpResponse(f'Placeholder to display blog number {number}.')

def edit_method(request, number):
    return HttpResponse(f'Placeholder to edit blog number {number}.')

def destroy_method(request, number):
    return redirect("/blogs")

def json_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})