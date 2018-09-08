from ..models import Useraddrs
from ..models import Users
from ..models import Feedback
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import requests
import json
import hashlib
import time
def getMyAddreses(request):
	user_id = request.session.get('user_id')
	resp=Useraddrs.objects.filter(user_id=user_id)
	json_data = serializers.serialize('json', resp)
	json_data = json.loads(json_data)
	return JsonResponse(json_data, safe=False)
def addMyAddreses(request):	
	user_id = request.session.get('user_id')
	resp=request.GET
	Useraddr=Useraddrs(user_id=user_id,address=resp['addr'],door=resp['door'],tel=resp['tel'],name=resp['name'])
	Useraddr.save()
	return JsonResponse({"state":0,"msg":"ok"})
def updateMyAddreses(request):
	user_id = request.session.get('user_id')
	resp=request.GET
	checked= 1 if resp.get('checked') else 0
	Useraddr=Useraddrs.objects.filter(user_id=user_id,id=resp['id']).update(address=resp['addr'],checked=checked,door=resp['door'],tel=resp['tel'],name=resp['name'])
	return JsonResponse({"state":0,"msg":"ok"})
def delMyAddreses(request):
	user_id = request.session.get('user_id')
	resp=request.GET
	Useraddr=Useraddrs.objects.filter(user_id=user_id,id=resp['id']).delete()
	return JsonResponse({"state":0,"msg":"ok"})
def getDefaultAddr(request):
	user_id = request.session.get('user_id')
	Useraddr=Useraddrs.objects.filter(user_id=user_id,checked=1).values()
	result=[]
	for x in Useraddr:
		result.append(x)
	return JsonResponse(result,safe=False)
def updateChecked(request):
	res = request.GET
	user_id = request.session.get('user_id')

	Useraddr=Useraddrs.objects.filter(user_id=user_id,checked=1).update(checked=0)
	Useraddr=Useraddrs.objects.filter(user_id=user_id,id=res['id']).update(checked=1)
	return JsonResponse({"state":0,"msg":"ok"})
def userauthor(request):

	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	}
	code=request.GET['code']
	APPID = settings.APPID
	APPSECRET = settings.APPSECRET
	url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code"%(APPID,APPSECRET,code)

	html=requests.get(url,headers=headers)
	html.encoding = 'utf-8'
	html_response = html.json()
	
	user = findUser(html_response['session_key'],html_response['openid'])
	if user:
		request.session['user_id']=user['id']
		request.session['user_uuid']=user['uuid']

	# session_key = request.session.session_key

	return JsonResponse(user)
def findUser(session_key,openid):
	result={}
	user = Users.objects.filter(openid=openid).values('id','uuid','avatarUrl','nickName')
	if user:
		result=user[0]
		result['newuser']=0
	else:
		salt=session_key+str(int(time.time()))
		md = hashlib.md5(salt.encode('utf-8'))  # bytes
		re = md.hexdigest()
		newuser=Users(uuid=re,openid=openid)
		newuser.save()
		result['id']=newuser.id
		result['uuid']=re
		result['newuser']=1
	return result
def setUserInfo(request):
	req = request.GET
	user_id = request.session.get('user_id')
	Users.objects.filter(user_id=user_id).update(avatarUrl=req['avatarUrl'],nickName=req['nickName'])
	return JsonResponse({"state":0,"msg":"ok"})
def FeedBack(request):
	req = request.GET
	print(req['device_system'])
	user_id = request.session.get('user_id',0)
	fb = Feedback(user_id=user_id,content=req['content'],contact=req['contact'],state=0,device_model=req['device_model']
		,device_system=req['device_system'],app_version=req['app_version'])
	fb.save()
	return JsonResponse({"state":0,"msg":"ok"})