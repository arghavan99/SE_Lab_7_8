from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from django.shortcuts import render

# Create your views here.
from apps.patient.models import Patient


def get_patient(request):
    national_id = request.data.get('national_id')
    p = Patient.objects.filter(national_id=national_id)
    if p is None:
        return Response(status=HTTP_404_NOT_FOUND)
    p = p[0]
    response = {
        'name': p.name,
        'email': p.email,
    }
    return JsonResponse(response, status=HTTP_200_OK)