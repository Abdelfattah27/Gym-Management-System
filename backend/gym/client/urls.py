from django.urls import path  
from . import views


urlpatterns = [
    path("all_clients_data/"  , views.get_all_clients_data) ,
    path("client_data/<str:pk>/"  , views.get_client_data) ,
    path("<str:pk>/absence/"  , views.mark_client_absent) ,
    path("add/" , views.add_client) ,
    path('<str:client_pk>/emergencycontacts/', views.emergency_contact_list_create),
    # path('<str:client_pk>/emergencycontacts/<str:pk>/', views.emergency_contact_detail),
    path('<str:client_pk>/medicalinformation/', views.medical_information_list_create),
    # path('<str:client_pk>/medicalinformation/<str:pk>/', views.medical_information_detail),
    path('<str:client_pk>/healthhistory/', views.health_history_list_create),
    # path('<str:client_pk>/healthhistory/<str:pk>/', views.health_history_detail),
    path('<str:client_pk>/fitnessassessments/', views.fitness_assessment_list_create),
    # path('<str:client_pk>/fitnessassessments/<str:pk>/', views.fitness_assessment_detail),
    path('<str:client_pk>/trainingplans/', views.training_plan_list_create),
    # path('<str:client_pk>/trainingplans/<str:pk>/', views.training_plan_detail),
    # path('<str:client_pk>/exercises/', views.exercise_list_create),
    # path('<str:client_pk>/exercises/<str:pk>/', views.exercise_detail),
    # path('<str:client_pk>/absences/', views.absence_list_create),
    # path('<str:client_pk>/absences/<str:pk>/', views.absence_detail),
    path('<str:client_pk>/muscleinformation/', views.muscle_information_list_create),
    # path('<str:client_pk>/muscleinformation/<str:pk>/', views.muscle_information_detail),
    path('<str:client_pk>/clientimages/', views.client_image_list_create),
    # path('<str:client_pk>/clientimages/<str:pk>/', views.client_image_detail),
    path('<str:client_pk>/latestclientimage/', views.client_last_image),
    path('<str:client_pk>/subscription/', views.client_subscription),
]
