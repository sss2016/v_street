from django.http import HttpResponse, JsonResponse
from ..models import Goods,Menu_Bns
from django.conf import settings
from . import file as my_file_tool
from django.core import serializers
import json
import datetime
def addGoods(request):
	user={"id":123,"Shops_id":456}
	json_result = request.POST
	file = request.FILES.get('file')
	good = Goods(
		name=json_result['goods_name'],
		price=json_result['goods_price'],
		shop_id=1,
		describe=json_result['dec'],
		stock=1,
		standards=json_result.get('guige'),
		type=int(json_result.get('type_id'))
		)
	good.save()
	state = my_file_tool.save_image(file,str(user['id'])+"_"+str(user['Shops_id'])+"_"+str(good.id))
	if state:
		return JsonResponse({"state":0,"msg":"ok"})
	Goods.objects.filter(id=good.id).delete()
	return JsonResponse({"state":1,"msg":"error"})
def getGoodsType(request):
	shop_id=1
	resp=Menu_Bns.objects.filter(shop_id=shop_id,delete_at=None)
	json_data = serializers.serialize('json', resp)
	json_data = json.loads(json_data)
	return JsonResponse({'json':json_data,'shop_id':shop_id}, safe=False)
def addType(request):
	req = json.loads(request.body) 
	Type=Menu_Bns(name=req['name'],shop_id=1)
	Type.save()
	return JsonResponse({"state":0,"msg":"ok"})
def deleteType(request):
	req = json.loads(request.body)
	now_time=datetime.datetime.now()
	delete_at=now_time.strftime('%Y-%m-%d')
	Menu_Bns.objects.filter(id__in=req['type_id']).update(delete_at=delete_at)
	return JsonResponse({"state":0,"msg":"ok"})
def getGoodsItem(request):
	getDatas = request.GET
	resp=Goods.objects.filter(shop_id=1,id=getDatas.get('goods_id'))
	json_data = serializers.serialize('json', resp)
	json_data = json.loads(json_data)
	return JsonResponse(json_data, safe=False)
def updateItem(request):
	req = json.loads(request.body)
	goods_id=req['goods_id']
	resKeys = req.keys()
	if 'standards' in resKeys:
		Goods.objects.filter(id=goods_id).update(standards=req['standards'])
	if 'name' in resKeys:
		Goods.objects.filter(id=goods_id).update(name=req['name'])
	if 'price' in resKeys:
		Goods.objects.filter(id=goods_id).update(price=req['price'])
	if 'type' in resKeys:
		Goods.objects.filter(id=goods_id).update(type=req['type'])
	if 'describe' in resKeys:
		Goods.objects.filter(id=goods_id).update(describe=req['describe'])
	return JsonResponse({"state":0,"msg":"ok"})
def deleteGoods(request):
	req = request.GET
	goods_id=req['goods_id']
	now_time=datetime.datetime.now()
	delete_at=now_time.strftime('%Y-%m-%d')
	Goods.objects.filter(id=goods_id).update(delete_at=delete_at)
	return JsonResponse({"state":0,"msg":"ok"})
def getFrontGoodsByshopId(request):
	req = request.GET
	shop_id=req['shop_id']
	result=[]
	typeid_name_arrays=Menu_Bns.objects.filter(shop_id=shop_id,delete_at=None).values('id','name')
	for x in range(len(typeid_name_arrays)):
		tmp = {}
		tmp['name']=typeid_name_arrays[x]['name']
		tmp['type']=typeid_name_arrays[x]['id']
		tmp['foods']=getGoodsByShop_type_Id(shop_id,typeid_name_arrays[x]['id'])
		result.append(tmp)
	return JsonResponse(result,safe=False)
def getGoodsByShop_type_Id(shop_id,type_id):
	arrays=Goods.objects.filter(shop_id=shop_id,delete_at=None,type=type_id).values()
	json_data=[]
	for x in range(len(arrays)):
		arrays[x]['Count']=0
		arrays[x]['the_count']=0
		arrays[x]['guige']=None
		
		json_data.append(arrays[x])
	return json_data
