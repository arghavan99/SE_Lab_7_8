from django.urls import path, include
from apps.doctor import views


app_name = "doctor"
urlpatterns = [
    path('get_doctor/', views.get_doctor, name='get_doctor'),
    path('get_new_doctors/', views.get_new_doctors, name='get_new_doctors'),
    path('get_doctor_signups/', views.get_doctor_signups, name='get_doctor_signups'),
    path('create_doctor/', views.create_doctor, name='create_doctor'),
    path('login_doctor/', views.login_doctor, name='login_doctor'),

]