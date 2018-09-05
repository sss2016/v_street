from django.http import HttpResponse, JsonResponse
from django.conf import settings
from ..models import Goods
import json 
import os

def save_image(file,name):
        with open(os.path.join(settings.BASE_DIR, 'static/goods_image', name),"wb")  as f:
            for chunk in file.chunks():
                f.write(chunk)
        return 1
def upload_image():
    pass
def getGoodsImage(request):
    user={
    "id":123,
    "Shops_id":456
    }
    Goods_id = request.GET.get('goods_id')
    name=str(user['id'])+"_"+str(user['Shops_id'])+"_"+str(Goods_id)
    imagepath=os.path.join(settings.BASE_DIR, 'static/goods_image', name)
    image_data = open(imagepath,"rb").read()
    return HttpResponse(image_data,content_type="image/png") #注意旧版的资料使用mimetype,现在已经改为content_type
