from django.urls import path, include
from apps.doctor import views


app_name = "doctor"
urlpatterns = [
    path('get_doctors/', views.get_doctors, name='get_doctor'),
    path('get_new_doctors/', views.get_new_doctors, name='get_new_doctors'),
    path('create_doctor/', views.create_doctor, name='create_doctor'),
    path('login_doctor/', views.login_doctor, name='login_doctor'),

]