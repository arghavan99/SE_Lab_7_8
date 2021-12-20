from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from prescription.models import Prescription

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
