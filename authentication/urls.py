from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('users/',views.get_all_users,name="get_all_users")
	
]