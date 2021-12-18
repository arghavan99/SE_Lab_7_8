from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_401_UNAUTHORIZED

from API_GATEWAY.settings import USER_MANAGEMENT_URL
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def register_doctor(request):
    name = request.POST['name']
    n_id = request.POST['national_id']
    password = request.POST['password']
    email = request.POST['email']
    username = request.POST['username']
    params = {'name': name, 'national_id':n_id, 'password': password, 'email': email, 'username':username}
    res = requests.post(USER_MANAGEMENT_URL + 'doctor/create_doctor/', data=params)
    if res.status_code == HTTP_201_CREATED:
        return Response(status=HTTP_201_CREATED)
    return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def register_patient(request):
    name = request.POST['name']
    n_id = request.POST['national_id']
    password = request.POST['password']
    email = request.POST['email']
    username = request.POST['username']
    params = {'name': name, 'national_id': n_id, 'password': password, 'email': email, 'username': username}
    res = requests.post(USER_MANAGEMENT_URL + 'patient/create_patient/', data=params)
    if res.status_code == HTTP_201_CREATED:
        return Response(status=HTTP_201_CREATED)
    return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_doctor(request):
    username = request.POST['username']
    password = request.POST['password']
    params = {'username': username, 'password': password}
    res = requests.post(USER_MANAGEMENT_URL + 'doctor/login_doctor/', data=params)
    # print('content', res.json())
    if res.status_code == 200:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_patient(request):
    username = request.POST['username']
    password = request.POST['password']
    params = {'username': username, 'password': password}
    res = requests.post(USER_MANAGEMENT_URL + 'patient/login_patient/', data=params)
    # print('content', res.json())
    if res.status_code == 200:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)
