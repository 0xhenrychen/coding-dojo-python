from django.shortcuts import render, redirect

from .models import Book, Author

def index(request):
    return render(request, "index.html")

# def add_dojo(request):
#     Dojo.objects.create(
#         name = request.POST["name"],
#         city = request.POST["city"],
#         state = request.POST["state"])
#     return redirect("/")

# def add_ninja(request):
#     Ninja.objects.create(
#         first_name = request.POST["first_name"],
#         last_name = request.POST["last_name"],
#         dojo = Dojo.objects.get(id = request.POST["dojo_id"]))
#     return redirect("/")