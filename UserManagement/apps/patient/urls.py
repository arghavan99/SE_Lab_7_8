from django.urls import path, include
from apps.patient import views


app_name = "patient"
urlpatterns = [
    path('get_patient/', views.get_patient, name='get_patient'),
    path('get_new_patients/', views.get_new_patients, name='get_new_patients'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('login_patient/', views.login_patient, name='login_patient'),
]