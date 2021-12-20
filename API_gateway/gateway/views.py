from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_401_UNAUTHORIZED, \
    HTTP_404_NOT_FOUND

from API_GATEWAY.settings import USER_MANAGEMENT_URL, PRESCRIPTION_MANAGEMENT_URL, AGGREGATOR_URL
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


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_admin(request):
    username = request.POST['username']
    password = request.POST['password']
    params = {'username': username, 'password': password}
    res = requests.post(USER_MANAGEMENT_URL + 'my_admin/login_admin/', data=params)
    # print('content', res.json())
    if res.status_code == 200:
        return JsonResponse(res.json(), status=HTTP_200_OK)
    return JsonResponse(res.json(), status=HTTP_401_UNAUTHORIZED)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def create_prescription(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        res_1 = requests.post(USER_MANAGEMENT_URL + 'get_user_permissions/', data={'token': token})
        if not res_1.json()['is_doctor']:
            return Response({'error': 'you are not a doctor!'}, status=HTTP_401_UNAUTHORIZED)
    except:
        return Response({'error': 'you are not a doctor'} ,status=HTTP_401_UNAUTHORIZED)
    n_id = request.POST['n_id']
    res_2 = requests.post(USER_MANAGEMENT_URL + 'patient/validate_patient/', data={'n_id':n_id})
    if res_2.status_code == 404:
        return Response({'error': 'no such patient'},status=HTTP_404_NOT_FOUND)
    params = {'d_id': res_1.json()['id'],
              'drug_list': request.POST['drug_list'],
              'comment': request.POST['comment'],
              'p_n_id': n_id}
    res = requests.post(PRESCRIPTION_MANAGEMENT_URL + 'create_prescription/', data=params)
    if res.status_code ==  HTTP_200_OK:
        return Response(status=HTTP_201_CREATED)
    else:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_prescriptions_for_doctor(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        res_1 = requests.post(USER_MANAGEMENT_URL + 'get_user_permissions/', data={'token': token})
        if not res_1.json()['is_doctor']:
            return Response({'error': 'you are not a doctor!'}, status=HTTP_401_UNAUTHORIZED)
    except:
        return Response({'error': 'you are not a doctor'} ,status=HTTP_401_UNAUTHORIZED)
    res_2 = requests.post(AGGREGATOR_URL + 'get_pres_for_doctor/', {'d_id': res_1.json()['id']})
    if res_2.status_code ==  HTTP_200_OK:
        return JsonResponse(res_2.json(), status=HTTP_200_OK, safe=False)
    else:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
