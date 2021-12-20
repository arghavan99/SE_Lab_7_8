from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django.utils.timezone import datetime
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


@api_view(["POST"])
@permission_classes((AllowAny,))
def get_doctors(request):
    ids = request.POST['ids']
    ids = ids.split(",")
    print(ids)
    d = Doctor.objects.filter(user_ptr_id__in=ids)
    serialized_doctor = DoctorSerializer(d, many=True)
    print(serialized_doctor.data)
    return JsonResponse(serialized_doctor.data, status=HTTP_200_OK, safe=False)


@api_view(["POST"])
@permission_classes((AllowAny,))
def get_new_doctors(request):
    docs = list(Doctor.objects.filter(date_joint=datetime.today()))
    serialized_doctors = DoctorSerializer(docs, many=True)
    print(serialized_doctors)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_doctors.data)
    return JsonResponse(serialized_doctors.data, status=HTTP_200_OK, safe=False)



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

