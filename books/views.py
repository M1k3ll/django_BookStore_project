from django.shortcuts import render

# Create your views here.
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
