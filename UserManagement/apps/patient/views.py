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
    HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
)

# Create your views here.
from apps.patient.models import Patient
from apps.patient.serializers import PatientSerializer

@api_view(["POST"])
@permission_classes((AllowAny,))
def get_new_patients(request):
    patients = list(Patient.objects.filter(date_joint=datetime.today()))
    serialized_patients = PatientSerializer(patients, many=True)
    print(serialized_patients)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_patients.data)
    return JsonResponse(serialized_patients.data, status=HTTP_200_OK, safe=False)

@api_view(["POST"])
@permission_classes((AllowAny,))
def get_patients(request):
    n_ids = request.POST['n_ids']
    n_ids = n_ids.split(",")
    print(n_ids)
    p = Patient.objects.filter(national_id__in=n_ids)
    serialized_patient = PatientSerializer(p, many=True)
    print(serialized_patient.data)
    return JsonResponse(serialized_patient.data, status=HTTP_200_OK, safe=False)





@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_patient(request):
    name = request.POST['name']
    n_id = request.POST['national_id']
    password = request.POST['password']
    email = request.POST['email']
    username = request.POST['username']
    try:
        p = Patient.objects.create(name=name, national_id=n_id, email=email, username=username)
        p.set_password(password)
        p.save()
        token = Token.objects.create(user=p)
        res = Response(status=HTTP_201_CREATED)
        return res
    except:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_patient(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def is_patient_valid(request):
    n_id = request.POST['n_id']
    p = Patient.objects.filter(national_id=n_id)
    if len(p) > 0:
        return Response(status=HTTP_200_OK)
    else:
        return Response(status=HTTP_404_NOT_FOUND)