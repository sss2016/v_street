from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt  # 解除csrf验证
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

conf = WechatConf(  # 实例化配置信息对象
    token='1736100',  # 服务器配置-Token
    appid='wx72fa0b87d2ba4704',  # 公众号开发信息-开发者ID
    appsecret='22843ca13f448b20709bc3bf57a284b2',  # 公众号开发信息-开发者密码
    encrypt_mode='normal',  # 服务器配置-明文模式
    encoding_aes_key='QlJv6tSAQA7ibvKA6roFgmpEsDI9xGoF1M5d90UHgOs'  # 服务器配置-EncodingAESKey
)


@csrf_exempt  # 去除csrf验证
def wechat(request):
    signature = request.GET.get('signature')  # 获取请求信息
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    wechat_instance = WechatBasic(conf=conf)  # 实例化微信基类对象
    if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):  # 检查验证请求的签名
        return HttpResponseBadRequest('Verify Failed')
    else:
        if request.method == 'GET':
            return HttpResponse(request.GET.get('echostr', None))  # 返回请求中的回复信息