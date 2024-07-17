from rest_framework import serializers
from .models import (
    Client,
    EmergencyContact,
    MedicalInformation,
    HealthHistory,
    FitnessAssessment,
    TrainingPlan,
    Exercise,
    Absence,
    MuscleInformation,
    ClientImage
)

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'

class MedicalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInformation
        fields = '__all__'

class HealthHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthHistory
        fields = '__all__'

class FitnessAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessAssessment
        fields = '__all__'

class TrainingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPlan
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

class MuscleInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleInformation
        fields = '__all__'

class ClientImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientImage
        fields = '__all__'

class ALLClientDataSerializer(serializers.ModelSerializer):
    emergency_contacts = EmergencyContactSerializer(many=True, read_only=True)
    medical_information = MedicalInformationSerializer(many=True, read_only=True)
    health_history = HealthHistorySerializer(many=True, read_only=True)
    fitness_assessments = FitnessAssessmentSerializer(many=True, read_only=True)
    training_plans = TrainingPlanSerializer(many=True, read_only=True)
    absences = AbsenceSerializer(many=True, read_only=True)
    muscle_information = MuscleInformationSerializer(many=True, read_only=True)
    images = ClientImageSerializer(many=True, read_only=True)
    
    def to_representation(self, instance):
        print(dir(instance))
        # Prefetch related objects to optimize database queries
        instance = Client.objects.prefetch_related(
            'emergency_contacts',
            'medical_information',
            'health_history',
            'fitness_assessments',
            'training_plans',
            'absences',
            'muscle_information',
            'images'
        ).get(pk=instance.pk)
        
        return super().to_representation(instance)

    class Meta:
        model = Client
        fields = '__all__'
        
        
class ClientSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Client
        fields = '__all__'
