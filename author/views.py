from django.shortcuts import render
from .models import Author

# Create your views here.
def get_all_authors(request):
	authors = Author.objects.order_by('id')
	context = {'authors':authors}
	return render(request, 'author/all_authors.html',context)

def delete_author(request):
	pass	