from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from apps.patient.models import Patient
from rest_framework.authtoken.models import Token
from apps.doctor.models import Doctor
from apps.my_admin.models import MyAdmin


@csrf_exempt
@api_view(["POST"])
def get_user_permissions(request):
    token = request.POST['token']
    try:
        user_id = Token.objects.filter(key=token)[0].user_id
    except:
        return JsonResponse({'error': 'false token'},status=HTTP_403_FORBIDDEN)
    p = Patient.objects.filter(user_ptr_id=user_id)
    d = Doctor.objects.filter(user_ptr_id=user_id)
    a = MyAdmin.objects.filter(user_ptr_id=user_id)
    if len(d) > 0:
        params = {'is_doctor': True, 'is_patient': False, 'is_admin': False, 'id': d[0].user_ptr_id}
    elif len(p) > 0:
        params = {'is_doctor': False, 'is_patient': True, 'is_admin': False, 'id': p[0].user_ptr_id}
    elif len(a) > 0:
        params = {'is_doctor': False, 'is_patient': False, 'is_admin': True, 'id': a[0].user_ptr_id}
    else:
        return JsonResponse({'error': 'false token'}, status=HTTP_403_FORBIDDEN)
    return JsonResponse(params, status=HTTP_200_OK)
