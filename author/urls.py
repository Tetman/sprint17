from django.urls import path
from . import views

urlpatterns = [
	# Домашняя страница
	path('authors/',views.get_all_authors,name="get_all_authors"),
	path('delete/',views.delete_author,name="delete_author")
]