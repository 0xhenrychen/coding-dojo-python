from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("add_book_form", views.add_book_form),
    path("books/<int:book_id>", views.book_page),
    path("authors", views.authors_page),
    path("add_author_form", views.add_author_form),
    path("authors/<int:author_id>", views.author_page)
    ]