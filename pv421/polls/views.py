import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print("__req", request)
    print("__req", request.method)
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.

@require_http_methods(['POST'])
@csrf_exempt
def poll(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse({
        "success": True,
        "data": data
    })
