from .views import RegisterAPI, ChangePasswordView
from django.urls import path

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('register/', RegisterAPI.as_view(), name='register'),
]
