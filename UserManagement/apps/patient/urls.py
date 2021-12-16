from django.urls import path, include
from apps.doctor import views


app_name = "patient"
urlpatterns = [
    path('get_patient/', views.get_doctor, name='get_patient'),
]