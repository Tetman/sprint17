from django.shortcuts import render
from .models import Order

# Create your views here.

def get_all_orders(request):
	orders = Order.objects.all()
	context = {'orders':orders}

	return render(request,'order/all_order.html',context)