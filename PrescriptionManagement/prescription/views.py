from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.utils.timezone import datetime
from prescription.models import Prescription
from prescription.serializers import PrescriptionSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_prescription(request):
    doctor_id = request.POST['d_id']
    p_n_id = request.POST['p_n_id']
    drug_list = request.POST['drug_list']
    comment = request.POST['comment']
    pres = Prescription.objects.create(doctor_id=doctor_id, patient_n_id = p_n_id, drug_list=drug_list, comment=comment)
    return Response(status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_prescriptions_for_doctor(request):
    doctor_id = request.POST['d_id']
    pres = list(Prescription.objects.filter(doctor_id=doctor_id))
    serialized_pres = PrescriptionSerializer(pres, many=True)
    print(serialized_pres)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_pres.data)
    return JsonResponse(serialized_pres.data, status=HTTP_200_OK, safe=False)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_prescriptions_for_patient(request):
    p_n_id = request.POST['p_n_id']
    pres = list(Prescription.objects.filter(patient_n_id=p_n_id))
    serialized_pres = PrescriptionSerializer(pres, many=True)
    print(serialized_pres)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_pres.data)
    return JsonResponse(serialized_pres.data, status=HTTP_200_OK, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_all_prescriptions(request):
    pres = list(Prescription.objects.all())
    serialized_pres = PrescriptionSerializer(pres, many=True)
    print(serialized_pres)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_pres.data)
    return JsonResponse(serialized_pres.data, status=HTTP_200_OK, safe=False)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_daily_pres(request):
    pres = list(Prescription.objects.filter(date_joint=datetime.today()))
    serialized_pres = PrescriptionSerializer(pres, many=True)
    print(serialized_pres)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_pres.data)
    return JsonResponse(serialized_pres.data, status=HTTP_200_OK, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_all_pres(request):
    pres = list(Prescription.objects.all())
    serialized_pres = PrescriptionSerializer(pres, many=True)
    print(serialized_pres)
    # res = JSONRenderer().render(serialized_pres.data)
    # print()
    print(serialized_pres.data)
    return JsonResponse(serialized_pres.data, status=HTTP_200_OK, safe=False)