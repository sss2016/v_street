from django.shortcuts import render

# Create your views here.
def getShop(request):
	return render(request,'shopinfo.html')
def index(request):
	return render(request,'index.html')