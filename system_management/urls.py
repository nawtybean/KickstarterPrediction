from django.urls import path
from system_management import views

urlpatterns = [
    path('', views.home, name='home'),
]
