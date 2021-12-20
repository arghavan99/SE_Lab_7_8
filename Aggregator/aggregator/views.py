import requests
from django.http import JsonResponse
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from aggregator.settings import PRESCRIPTION_MANAGEMENT_URL, USER_MANAGEMENT_URL


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def get_prescription_list_for_doctor(request):
    doctor_id = request.POST['d_id']
    res = requests.post(PRESCRIPTION_MANAGEMENT_URL + 'get_pres_for_doctor/', {'d_id': doctor_id})
    prescriptions = res.json()
    print('list of prescriptions:', prescriptions)
    list_of_p_n_ids = [x['patient_n_id'] for x in prescriptions]
    list_of_p_n_ids = ",".join(list_of_p_n_ids)
    print(list_of_p_n_ids)
    res_2 = requests.post(USER_MANAGEMENT_URL + 'patient/get_patients/', {'n_ids': list_of_p_n_ids})
    patients = {}
    for p in res_2.json():
        patients.update({p['national_id'] : p['name']})
    print(patients)
    for p in prescriptions:
        del p['doctor_id']
        p['patient_info'] = patients[p['patient_n_id']]
        del p['patient_n_id']
    print(prescriptions)
    return JsonResponse(prescriptions, status=HTTP_200_OK, safe=False)
