from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse
from ..models import Goods
import json 
from django.core import serializers

def showIndex(request):
	return render(request,'index.html')
def getGoodsList(request):
	# all_message = Goods.objects.filter(name=u"王二小",address=u"杭州")
	resp = Goods.objects.filter(type=request.GET.get('type_id'),shop_id=1,delete_at=None)
	json_data = serializers.serialize('json', resp)
	json_data = json.loads(json_data)
	return JsonResponse(json_data, safe=False)

