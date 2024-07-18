from django.contrib import admin
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

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'home_phone', 'address', 'occupation', 'date_of_birth', 'work_phone', 'created_by', 'updated_by', 'day_number')
    search_fields = ('name', 'home_phone')

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'phone', 'relationship')
    search_fields = ('client__name', 'name', 'phone')

@admin.register(MedicalInformation)
class MedicalInformationAdmin(admin.ModelAdmin):
    list_display = ('client', 'physician', 'physician_phone', 'under_care', 'taking_medication', 'high_blood_pressure', 'bone_joint_problem', 'vigorous_exercise', 'chest_pain')
    search_fields = ('client__name', 'physician')

@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ('client', 'asthma', 'respiratory_conditions', 'diabetes', 'epilepsy', 'osteoporosis')
    search_fields = ('client__name',)

@admin.register(FitnessAssessment)
class FitnessAssessmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'blood_pressure', 'resting_heart_rate', 'high_estimate_heart_rate', 'cardiovascular_test_name', 'cardiovascular_test_result')
    search_fields = ('client__name', 'cardiovascular_test_name')

@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('client', 'level', 'frequency', 'date', 'created_by', 'updated_by')
    search_fields = ('client__name', 'level')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('training_plan', 'day', 'exercise_name', 'reps', 'sets', 'rest', 'created_by', 'updated_by')
    search_fields = ('training_plan__client__name', 'exercise_name')

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'reason')
    search_fields = ('client__name',)

@admin.register(MuscleInformation)
class MuscleInformationAdmin(admin.ModelAdmin):
    list_display = ('client', 'muscle_group', 'size', 'date')
    search_fields = ('client__name', 'muscle_group')

@admin.register(ClientImage)
class ClientImageAdmin(admin.ModelAdmin):
    list_display = ('client', 'image_path', 'date')
    search_fields = ('client__name',)
# from authen.models import User    
# admin.site.register(User)