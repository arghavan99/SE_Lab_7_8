from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.
from apps.patient.models import Patient
from apps.patient.serializers import PatientSerializer


def get_patient(request):
    national_id = request.data.get('national_id')
    p = Patient.objects.filter(national_id=national_id)
    if p is None:
        return Response(status=HTTP_404_NOT_FOUND)
    p = p[0]
    serialized_patient = PatientSerializer(p)
    print(serialized_patient.data)
    res = JSONRenderer().render(serialized_patient.data)
    return JsonResponse(res, status=HTTP_200_OK)

@user_passes_test(lambda u: u.is_superuser)
def get_new_patients(request):
    patients = reversed(Patient.objects.all().order_by('-id')[:5])
    serialized_patients = PatientSerializer(patients, many=True)
    print(serialized_patients.data)
    res = JSONRenderer().render(serialized_patients.data)
    return JsonResponse(res, status=HTTP_200_OK)


def create_patient(request):
    name = request.data.get('name')
    n_id = request.data.get('national_id')
    password = request.data.get('password')
    email = request.data.get('email')
    p = Patient.objects.create(name=name, national_id=n_id, email=email, commit=False)
    p.set_password(password)
    p.save() #todo Chcek
    return Response(HTTP_200_OK)
