from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html'),name='patientlogin'),
    path('patientsignup', views.patient_signup_view,name='patientsignup'),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('make-request', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
    
     ##reset password##
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]