from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse
from ..models import Goods
from ..models import Swiperdata
import json 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

def showIndex(request):
	return render(request,'index.html')
def getGoodsList(request):
	shop_id = 456
	# all_message = Goods.objects.filter(name=u"王二小",address=u"杭州")
	size = request.GET.get('size')
	page = request.GET.get('page')
	resp = Goods.objects.filter(type=request.GET.get('type_id'),shop_id=1,delete_at=None)
	paginator = Paginator(resp, int(size))
	# resp=Shops.objects.filter(delete_at=None)
	if page:
		Shop = paginator.page(page).object_list
	else:
		Shop = paginator.page(1).object_list
	json_data = {
		"data":serializers.serialize("json", Shop, ensure_ascii=False),
		"pages":paginator.num_pages
	}
	# json_ = serializers.serialize("json", json_data, ensure_ascii=False)
	# {:json_data,pages:}
	# return JsonResponse(json_data,safe=False)
	# json_data = serializers.serialize('json', resp)
	# json_data = json.loads(json_data)
	return JsonResponse(json_data, safe=False)

def getSwiper(request):
	resp=Swiperdata.objects.filter(state=1)
	json_data = serializers.serialize('json', resp)
	json_data = json.loads(json_data)
	return JsonResponse(json_data, safe=False)
