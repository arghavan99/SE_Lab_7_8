from django.views.generic import RedirectView
from django.urls import path, include

from prescription import views


app_name = "prescription"
urlpatterns = [
    path('create_prescription/', views.create_prescription),
    path('get_pres_for_doctor/', views.get_prescriptions_for_doctor),
    path('get_pres_for_patient/', views.get_prescriptions_for_patient),
    path('get_daily_pres/', views.get_daily_pres),
   path('get_all_pres/', views.get_all_pres),
]