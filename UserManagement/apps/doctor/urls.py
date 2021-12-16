from django.urls import path, include
from apps.doctor import views


app_name = "doctor"
urlpatterns = [
    path('get_doctor/', views.get_doctor, name='get_doctor'),
    path('get_new_doctors/', views.get_new_doctors, name='get_new_doctors'),
]