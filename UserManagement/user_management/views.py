from django.http import JsonResponse
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from apps.patient.models import Patient
from rest_framework.authtoken.models import Token
from apps.doctor.models import Doctor


def get_user_permissions(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
    try:
        user_id = Token.objects.filter(key=token)[0].user_id
    except:
        return JsonResponse({'error': 'false token'},status=HTTP_403_FORBIDDEN)
    p = Patient.objects.filter(user_ptr_id=user_id)
    d = Doctor.objects.filter(user_ptr_id=user_id)
    if len(d) > 0:
        params = {'is_doctor': True, 'is_patient': False}
    elif len(p) > 0:
        params = {'is_doctor': False, 'is_patient': True}
    else:
        return JsonResponse({'error': 'false token'}, status=HTTP_403_FORBIDDEN)
    return JsonResponse(params, status=HTTP_200_OK)
