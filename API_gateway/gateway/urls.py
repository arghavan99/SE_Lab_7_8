from django.views.generic import RedirectView
from django.urls import path, include

from API_GATEWAY.settings import USER_MANAGEMENT_URL
from gateway import views


app_name = "gateway"
urlpatterns = [
    path('register_doctor/', views.register_doctor),
    path('register_patient/', views.register_patient),
    path('login_doctor/', views.login_doctor),
    path('login_patient/', views.login_patient),
    path('login_admin/', views.login_admin),
    path('create_prescription/', views.create_prescription),
    path('get_prescriptions_for_doctor/', views.get_prescriptions_for_doctor),
    path('get_prescriptions_for_patient/', views.get_prescriptions_for_patient),
    path('get_prescriptions_for_admin/', views.get_prescriptions_for_admin),
    path('get_daily_prescriptions_count/', views.get_prescription_count),
    path('get_daily_new_users/', views.get_new_users),
    path('get_daily_doctor_signups/', views.get_doctor_signups),
]