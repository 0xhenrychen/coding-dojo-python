from django.shortcuts import render, HttpResponse
# def index(request):
#     # return HttpResponse("this is the equivalent of @app.route('/')!")
#     return HttpResponse("response from index method from root route, localhost:8000!")

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"],
    }
    return render(request, "index.html", context)

def first_name(request, first_name):
    context = {
        "first_name": first_name,
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"],
    }
    return render(request, "index2.html", context)
