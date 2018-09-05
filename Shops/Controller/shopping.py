from ..models import Orders
from ..models import Sales
import time
from django.db import transaction
from ..models import Shops
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# columns = Column.objects.all()
# articles = Article.objects.all()


def getShops(request):

	resp=Shops.objects.filter(delete_at=None)
    # cus_list = Article.objects.all()
	paginator = Paginator(resp, 3)
	page = request.GET.get('page')
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