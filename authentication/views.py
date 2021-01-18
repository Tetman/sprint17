from django.shortcuts import render
from .models import CustomUser

def index(request):
	return render(request,'index.html')

def get_all_users(request):
	users = CustomUser.objects.order_by('id')
	context = {'users':users}
	return render(request,'user/all_user.html',context)
