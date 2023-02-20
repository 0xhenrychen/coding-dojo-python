from django.shortcuts import render, HttpResponse
def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    return HttpResponse("response from index method from root route, localhost:8000!")
