from ..models import Orders
from ..models import Sales
from ..models import Goods
import time
from django.db import transaction
from ..models import Shops
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import radians, cos, sin, asin, sqrt
from django.db.models import Count
from django.db.models import Sum

# columns = Column.objects.all()
# articles = Article.objects.all()


def getShops(request):

    # cus_list = Article.objects.all()
	size = request.GET.get('size')
	page = request.GET.get('page')
	searchVal = request.GET.get('searchVal')
	latitude = request.GET.get('latitude')
	longitude=request.GET.get('longitude')
	sort_raw = request.GET.get('sort_raw')
	resp = ShopFilter(searchVal,latitude,longitude,sort_raw)
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
	return JsonResponse(json_data,safe=False)
def QueySetToJSON(QueySet):
	result=[]
	for x in QueySet:
		result.append(x.values())
	return result
def submitOrder(request):
	user_id = request.session.get('user_id')
	req = request.GET
	ordernum =time.strftime("%Y%m%d%H%M%S", time.localtime()) 
	ordernum+=str(user_id)

# 销量增加
	try:
		Shop = Shops.objects.get(id=req['shop_id'])
		Shop.sales=Shop.sales+1
		Shop.save()
		simpleInfo=addSales(req['shop_car'],req['shop_id'],ordernum,user_id)
		Order=Orders(ordernum=ordernum,shop_id=req['shop_id'],
		state=0,total=req['total'],user_id=user_id,shop_name=req['shop_name'],sendway=req['sendway'],payway=req['payway'],
		address=req['address'],user_name=req['user_name'],tel=req['tel'],simpleInfo=simpleInfo
		)
		Order.save()
	except:
		print("back")
		transaction.rollback()
	
	return JsonResponse({"state":0,"msg":"ok"})
def addSales(goods,shop_id,ordernum,user_id):
	datas = json.loads(goods)
	simpleInfo = datas[0]['name']
	num = 0
	for item in datas:
		Sale = Sales(Orders_id=ordernum,user_id=user_id,goods_id=int(item['id']),goods_name=item['name'],price=float(item['price']),
			count=int(item['num']),shop_id=shop_id,standards=item['guige_json'])
		num+=int(item['num'])
		Sale.save()
	if num>1:
		simpleInfo+="等"+str(num)+"件物品"
	return simpleInfo;
def getOrderList(request):
	user_id = request.session.get('user_id')
	print(user_id)
	order = Orders.objects.filter(user_id=user_id).order_by('-create_at').values()
	result=[]
	for x in range(len(order)):
		tmp = order[x]
		tmp['shop_name']=Shops.objects.filter(id=1).values()[0]['name']
		result.append(tmp)
	# json_data = serializers.serialize('json', order)
	return JsonResponse(result, safe=False)
def cancelOrder(request):
	req=request.GET
	order = Orders.objects.filter(ordernum=req['ordernum']).update(state=4)
	return JsonResponse({"state":0,"msg":"ok"})
def getOrderDetail(request):
	req=request.GET

	order = Orders.objects.filter(ordernum=req['ordernum']).values()
	result=dict(order[0])
	result['Sales']=getSaleRecord(req['ordernum'])
	return JsonResponse(result,safe=False)
def getSaleRecord(ordernum):
	result=[]
	Sale=Sales.objects.filter(Orders_id=ordernum).values()
	for x in Sale:
		result.append(x)
	return result
def ShopFilter(searchVal,latitude,longitude,sort_raw):
	val = searchVal
	result=None
	resp = None
	if val:
		ids = Goods.objects.filter(delete_at=None,name__contains=val).values_list('shop_id')
		in_id=[]
		for id_ in ids:
			in_id.append(id_[0])
		resp=Shops.objects.filter(Q(delete_at=None)&Q(name__contains=val) | Q(door__contains=val)|Q(id__in=in_id))
	else:
		resp=Shops.objects.filter(delete_at=None)
	lists=resp
	sort_raw=int(sort_raw)
	if sort_raw==0:
		# 综合排序
		result=lists.order_by("sales", "initial_price","distribution_price","name")
	elif sort_raw==1:
		result=lists.order_by("initial_price")
	elif sort_raw==2:
		result=lists.order_by("distribution_price")
	elif sort_raw==3:
		result=lists.order_by("sales")
	elif sort_raw==4:
		result=lists.order_by("name")
	return result
def setDistanceField(QueySet_,latitude,longitude):
	for qt in QueySet_:
		qt['Distance']=haversine(float(longitude),float(latitude),float(qt['longitude']),float(qt['latitude']))
	return QueySet_
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000
def getShopDetail(request):
	resp = request.GET
	resp=Shops.objects.filter(id=resp.get('shop_id')).values()[0]
	return JsonResponse(resp,safe=False)
def findOrders(request):
	req = request.GET
	search_rule = req['rule']
	Order_list=Orders.objects.filter(Q(ordernum__contains=search_rule)|Q(user_name__contains=search_rule)|Q(tel__contains=search_rule)).order_by("create_at")
	json_data = serializers.serialize('json',Order_list)
	res = json.loads(json_data)
	return JsonResponse(res,safe=False)
def getMyOrderByType(request):
	req = request.GET
	type_ = req.get('type',0)
	if int(type_)==-1:
		resp = Orders.objects.filter(Q(shop_id=1)&~Q(state=0)&Q(delete_at=None))
	else:
		resp = Orders.objects.filter(shop_id=1,state = type_,delete_at=None)
	json_data = serializers.serialize('json', resp)
	json_data = json.loads(json_data)
	return JsonResponse(json_data,safe=False)
def alterOrderState(request):
	req = request.GET
	state = req.get('state')
	ordernum = req.get('ordernum')
	R = Orders.objects.filter(shop_id=1,ordernum=ordernum,delete_at=None)
	R.update(state=state)
	return JsonResponse({"state":state,"msg":"ok"})
def denyOrder(request):
	req = request.GET
	state = req.get('state')
	ordernum = req.get('ordernum')
	reason = req.get('reason')
	R = Orders.objects.filter(shop_id=1,ordernum=ordernum,delete_at=None).update(state=state,reason=reason)
	return JsonResponse({"state":state,"msg":"ok"})
def getMyCount(request):
	shop_id=1
	res = Orders.objects.filter(Q(shop_id=1)&~Q(state=0)&Q(delete_at=None)).values('shop_id','total')
	count = res.annotate(num=Sum('total'),Alltotal=Count('shop_id'))
	# json_data = serializers.serialize('json', count)
	# json_data = json.loads(json_data)
	return JsonResponse({"num":count[0]['num'],"Alltotal":count[0]['Alltotal']})