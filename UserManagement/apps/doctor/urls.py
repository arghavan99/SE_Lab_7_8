from django.urls import path, include
from apps.doctor import views


app_name = "doctor"
urlpatterns = [
    path('get_doctor/', views.get_doctor, name='get_doctor'),
]