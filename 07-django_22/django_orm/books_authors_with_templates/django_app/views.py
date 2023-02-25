from django.shortcuts import render, redirect

from .models import Book, Author

##### Books #####

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "book_add.html", context)

def add_book_form(request):
    Book.objects.create(
        title = request.POST["title"],
        desc = request.POST["description"]
    )
    return redirect("/")

def book_page(request, book_id):
    context = {
        "this_book": Book.objects.get(id=book_id),
        "all_authors": Author.objects.all()
    }
    return render(request, "book_view.html", context)

##### Authors #####

def authors_page(request):
     context = {
        "all_authors": Author.objects.all()
    }
     return render(request, "author_add.html", context)

def author_page(request, author_id):
    context = {
        "this_author": Author.objects.get(id=author_id)
    }
    return render(request, "author_view.html", context)

def add_author_form(request):
    Author.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        notes = request.POST["notes"]
        # dojo = Dojo.objects.get(id = request.POST["dojo_id"]))
    )
    return redirect("/authors")