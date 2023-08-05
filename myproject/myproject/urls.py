from django.urls import path
from . import views

urlpatterns = [
    path('student_registration/', views.student_registration, name="student_registration"),
    path('registration_management/', views.registration_management, name="registration_management"),
    path('sport_management/', views.sport_management, name="sport_management"),
    path('generate_reports/', views.generate_reports, name="generate_reports"),
]
