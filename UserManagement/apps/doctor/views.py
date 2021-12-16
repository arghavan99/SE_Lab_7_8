from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from django.shortcuts import render

# Create your views here.
from apps.doctor.models import Doctor


def get_doctor(request):
    national_id = request.data.get('national_id')
    d = Doctor.objects.filter(national_id=national_id)
    if d is None:
        return Response(status=HTTP_404_NOT_FOUND)
    d = d[0]
    response = {
        'name': d.name,
        'email': d.email,
    }
    return JsonResponse(response, status=HTTP_200_OK)