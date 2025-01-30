from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def test(request:HttpRequest) -> JsonResponse:
    return JsonResponse(data={"SUCCES": "todo parece estar correcto"}, status=201)