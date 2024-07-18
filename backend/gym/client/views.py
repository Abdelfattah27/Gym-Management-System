from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from .serializers import ALLClientDataSerializer , ClientSerializer
from .models import Client , Absence
from django.utils import timezone
from django.db import IntegrityError
from .helper import generate_password
from authen.models import User
from rest_framework import status
from datetime import timedelta

@permission_classes([IsAdminUser]) 
@api_view(["GET"] )
def get_all_clients_data(request) : 
    print(request.user)
    clients = Client.objects.all()
    serializer = ALLClientDataSerializer(clients , many=True) 
    
    return Response(serializer.data , status=200)

@permission_classes([IsAdminUser]) 
@api_view(["GET"] )
def get_client_data(request , pk) : 
    
    client = Client.objects.filter(id=pk).first()
    if client is None : 
        return Response({"detail" : "No Client with this id"} , status=404)
    
    serializer = ALLClientDataSerializer(client) 
    
    return Response(serializer.data , status=200)




@permission_classes([IsAdminUser]) 
@api_view(["POST"] )
def mark_client_absent(request , pk) : 
    try : 
        data = request.data 
        Absence.objects.create(
            client_id=pk,
            date=data.get("date" , timezone.now().date()),
            reason=data.get("reason" , None)
        )
        return Response({"detail" : "marked as absent"} , status=201)
    except IntegrityError as ex:
        if str(ex).find("UNIQUE") != -1 : 
            return Response({"detail": "Marked Absent Before"}, status=400)
        elif str(ex).find("FOREIGN") != -1  : 
            return Response({"detail": "No Client With this id"}, status=404)
        else : 
            return Response({"detail" : f"error had happen {str(ex)}" } , status=400)
    except Exception as ex : 
        return Response({"detail" : f"error had happen {str(ex)}" } , status=400)



@permission_classes([IsAdminUser]) 
@api_view(["POST"] )
def add_client(request ) : 
    data = request.data 
    data["created_by"] = request.user.id
    current_date = timezone.now().date()
    
    subscription_durations = {
        "MONTHLY": timedelta(days=30),
        "YEARLY": timedelta(days=365),
        "DAILY": timedelta(days=1),
    }
    
    # Set the start date to now if not provided
    data["subscription_start_date"] = data.get("subscription_start_date", current_date)
    
    # Calculate the end date based on the subscription plan
    if subscription_plan in subscription_durations:
        data["subscription_end_date"] = data["subscription_start_date"] + subscription_durations[subscription_plan]
    else:
        # Default end date if the subscription plan is not recognized
        data["subscription_end_date"] = data.get("subscription_end_date", current_date)
    
    # subscription_plan = data.get("subscription_plan")
    # if subscription_plan == "MONTHLY" : 
    #     data["subscription_start_data"] = data.get("subscription_start_data" , timezone.now().date)
    #     data["subscription_end_data"] = data.get("subscription_end_data" , timezone.now().date)
    
    serializer = ClientSerializer(data=data)
    if serializer.is_valid () :
        
        client = serializer.save()
        password = generate_password() 
        username = data.get("name").replace(" " , "").lower() + str(client.id) 
        
        
        User.objects.create_user(username=username , password=password)
        user_data = {
            "username" :  username , 
            "password" : password , 
            "id" : client.id
        }
        return Response(user_data , status=202)
    else : 
        return Response(serializer.errors , status=400)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Generic function-based views for CRUD operations with client pk
def list_create_view(request, client_pk, model, serializer_class):
    if request.method == 'GET':
        instances = model.objects.filter(client_id=client_pk)
        serializer = serializer_class(instances, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        data['client'] = client_pk
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def retrieve_update_delete_view(request, client_pk, pk, model, serializer_class):
    try:
        instance = model.objects.get(pk=pk, client_id=client_pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializer_class(instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data.copy()
        data['client'] = client_pk
        serializer = serializer_class(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Specific views for each model
@api_view(['GET', 'POST'])
def emergency_contact_list_create(request, client_pk):
    return list_create_view(request, client_pk, EmergencyContact, EmergencyContactSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def emergency_contact_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, EmergencyContact, EmergencyContactSerializer)

@api_view(['GET', 'POST'])
def medical_information_list_create(request, client_pk):
    return list_create_view(request, client_pk, MedicalInformation, MedicalInformationSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def medical_information_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, MedicalInformation, MedicalInformationSerializer)

@api_view(['GET', 'POST'])
def health_history_list_create(request, client_pk):
    return list_create_view(request, client_pk, HealthHistory, HealthHistorySerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def health_history_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, HealthHistory, HealthHistorySerializer)

@api_view(['GET', 'POST'])
def fitness_assessment_list_create(request, client_pk):
    return list_create_view(request, client_pk, FitnessAssessment, FitnessAssessmentSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def fitness_assessment_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, FitnessAssessment, FitnessAssessmentSerializer)

@api_view(['GET', 'POST'])
def training_plan_list_create(request, client_pk):
    return list_create_view(request, client_pk, TrainingPlan, TrainingPlanSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def training_plan_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, TrainingPlan, TrainingPlanSerializer)

# @api_view(['GET', 'POST'])
# def exercise_list_create(request, client_pk):
#     return list_create_view(request, client_pk, Exercise, ExerciseSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def exercise_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, Exercise, ExerciseSerializer)

# @api_view(['GET', 'POST'])
# def absence_list_create(request, client_pk):
#     return list_create_view(request, client_pk, Absence, AbsenceSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def absence_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, Absence, AbsenceSerializer)

@api_view(['GET', 'POST'])
def muscle_information_list_create(request, client_pk):
    return list_create_view(request, client_pk, MuscleInformation, MuscleInformationSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def muscle_information_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, MuscleInformation, MuscleInformationSerializer)

# @api_view(['GET', 'POST'])
# def client_image_list_create(request, client_pk):
#     return list_create_view(request, client_pk, ClientImage, ClientImageSerializer)

# @api_view(['GET', 'PUT', 'DELETE'])
# def client_image_detail(request, client_pk, pk):
#     return retrieve_update_delete_view(request, client_pk, pk, ClientImage, ClientImageSerializer)

        
    
@permission_classes([IsAdminUser])
@api_view(["POST" , "GET"])
def client_image_list_create(request , client_pk):
    try:
        if request.method == "POST" : 
            image = request.FILES.get("image")
            if client_pk and image:
                client_image = ClientImage(client_id = client_pk )
                client_image.image_path.save(image.name, image)
                client_image.save()
                
                # serializer = ProductSerializer(product)
                return Response({"detail" : "Image Saved Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Parameter(s) missing"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "GET" : 
            
            images = ClientImage.objects.filter(client_id = client_pk) 
            serializer = ClientImageSerializer(images , many=  True)
            return Response(serializer.data , status=200)
        
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@permission_classes([IsAdminUser , IsAuthenticated])
@api_view(["GET"])  
def client_last_image(request , client_pk) :
    if request.user.is_superuser or request.user.client_id == client_pk :  
        latest_image = ClientImage.objects.filter(client_id =client_pk ).order_by('-date').first()
        if latest_image : 
            serializer = ClientImageSerializer(latest_image)
            return Response(serializer.data , status=200)
        else : 
            return Response({"detail" : "No Images for that user" } , status=404)
    else : 
        return Response({"detail" : "Not Authorized"} , status=status.HTTP_403_FORBIDDEN)

def client_subscription(request , client_id) : 
    if request.method == "GET" : 
        client = Client.objects.filter(id=client_id).only("name" , "subscription_plan", "subscription_start_data", "subscription_end_data").first()
        status = client.subscription_end_data <= timezone.now().date
        if client : 
            data = {
                "name" : client.name , 
                "subscription_plan" : client.subscription_plan ,
                "subscription_start_data" : client.subscription_start_data , 
                "subscription_end_data" : client.subscription_end_data , 
                "status" : status
              }
            return Response(data , status=200)
        else : 
            return Response({"detail" : "No CLient With this id"} , status=404) 
         