from django.shortcuts import render
from .models import Book


def get_all_books(request):
	books = Book.objects.all()
	context = {'books':books}

	return render(request,'book/all_books.html',context)
