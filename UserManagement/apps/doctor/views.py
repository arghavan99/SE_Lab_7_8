from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.
from apps.doctor.models import Doctor
from apps.doctor.serializers import DoctorSerializer


def get_doctor(request):
    national_id = request.data.get('national_id')
    d = Doctor.objects.filter(national_id=national_id)
    if d is None:
        return Response(status=HTTP_404_NOT_FOUND)
    d = d[0]
    serialized_doctor = DoctorSerializer(d)
    print(serialized_doctor.data)
    res = JSONRenderer().render(serialized_doctor.data)
    return JsonResponse(res, status=HTTP_200_OK)

@user_passes_test(lambda u: u.is_superuser)
def get_new_doctors(request):
    doctors = reversed(Doctor.objects.all().order_by('-id')[:5])
    serialized_doctors = DoctorSerializer(doctors, many=True)
    print(serialized_doctors.data)
    res = JSONRenderer().render(serialized_doctors.data)
    return JsonResponse(res, status=HTTP_200_OK)


def get_doctor_signups(request):
    doctors = Doctor.objects.all()
    serialized_doctors = DoctorSerializer(doctors, many=True)
    print(serialized_doctors.data)
    res = JSONRenderer().render(serialized_doctors.data)
    return JsonResponse(res, status=HTTP_200_OK)


def create_doctor(request):
    name = request.data.get('name')
    n_id = request.data.get('national_id')
    password = request.data.get('password')
    email = request.data.get('email')
    d = Doctor.objects.create(name=name, national_id=n_id, email=email, commit=False)
    d.set_password(password)
    d.save() #todo Chcek
    return Response(HTTP_200_OK)






