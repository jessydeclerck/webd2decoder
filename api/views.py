from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from decoder import main

@csrf_exempt
@require_http_methods(["POST"])
def decodeFromServer(request):
    data = request.body.decode('utf-8')
    return JsonResponse(main.readMsg(data, False))

@csrf_exempt
@require_http_methods(["POST"])
def decodeFromClient(request):
    data = request.body.decode('utf-8')
    return JsonResponse(main.readMsg(data, True))
