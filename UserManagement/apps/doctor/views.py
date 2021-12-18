from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

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

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_doctor(request):
    name = request.POST['name']
    n_id = request.POST['national_id']
    password = request.POST['password']
    email = request.POST['email']
    username = request.POST['username']
    try:
        d = Doctor.objects.create(name=name, national_id=n_id, email=email, username=username)
        d.set_password(password)
        token = Token.objects.create(user=d)
        d.save()
        res = Response(status=HTTP_201_CREATED)
        return res
    except:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_doctor(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return JsonResponse({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return JsonResponse({'token': token.key},
                    status=HTTP_200_OK)




