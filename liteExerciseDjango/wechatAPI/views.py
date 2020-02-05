from django.http import HttpResponse
import json


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the assetinfo index.")


def get_random_sport(request):
    """
    获取随机运动的接口
    :param request:
    :return:
    """
    print(request.body)
    result = {"msg": "半膝俯卧撑10个"}
    if request.method == 'POST':
        result["methods"] = "POST"
        return HttpResponse(json.dumps(result, ensure_ascii=False),
                            content_type="application/json, charset=utf-8")
    else:
        result = {"msg": "请求方式错误"}
        return HttpResponse(json.dumps(result, ensure_ascii=False),
                            content_type="application/json, charset=utf-8")
