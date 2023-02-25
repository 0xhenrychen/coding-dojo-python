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
        "all_authors": Author.objects.all(),
        "all_authors_for_this_book": Book.objects.get(id=book_id).authors.all()
    }
    return render(request, "book_view.html", context)

def add_book_to_author_form(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_book = Book.objects.get(id=request.POST["book_id"])
    this_book.authors.add(this_author)
    return redirect(f'/authors/{ author_id }')

##### Authors #####

def authors_page(request):
     context = {
        "all_authors": Author.objects.all()
    }
     return render(request, "author_add.html", context)

def author_page(request, author_id):
    context = {
        "this_author": Author.objects.get(id=author_id),
        "all_books": Book.objects.all(),
        "all_books_for_this_author": Author.objects.get(id=author_id).books.all()
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

def add_author_to_book_form(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=request.POST["author_id"])
    this_author.books.add(this_book)
    return redirect(f'/books/{ book_id }')