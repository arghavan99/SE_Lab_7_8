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
]