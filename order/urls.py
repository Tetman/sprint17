from django.urls import path
from . import views
urlpatterns = [
	path('',views.get_all_orders,name='get_all_orders')
]