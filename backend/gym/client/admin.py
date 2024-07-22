from gym.admin import CustomModelAdmin
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

class EmergencyContactTabular(admin.TabularInline) : 
    per_page = 15
    # template = 'admin/edit_inline/tabuler_with_paginator.html'
    model = EmergencyContact
    # fields = ["topic" ]
    # form = OrganizationTopicsForm
    # readonly_fields = [ "display_person_data" , "display_picture"]
    can_delete = True
    verbose_name_plural = "EmergencyContact"
    extra = 0
    classes = ["wide"]
class MedicalInformationTabular(admin.TabularInline) : 
    per_page = 15
    # template = 'admin/edit_inline/tabuler_with_paginator.html'
    model = MedicalInformation
    # fields = ["topic" ]
    # form = OrganizationTopicsForm
    # readonly_fields = [ "display_person_data" , "display_picture"]
    can_delete = True
    verbose_name_plural = "MedicalInformation"
    extra = 0
    classes = ["wide"]
class HealthHistoryTabular(admin.TabularInline) : 
    per_page = 15
    # template = 'admin/edit_inline/tabuler_with_paginator.html'
    model = HealthHistory
    # fields = ["topic" ]
    # form = OrganizationTopicsForm
    # readonly_fields = [ "display_person_data" , "display_picture"]
    can_delete = True
    verbose_name_plural = "HealthHistory"
    extra = 0
    classes = ["wide"]
class FitnessAssessmentTabular(admin.TabularInline) : 
    per_page = 15
    # template = 'admin/edit_inline/tabuler_with_paginator.html'
    model = FitnessAssessment
    # fields = ["topic" ]
    # form = OrganizationTopicsForm
    # readonly_fields = [ "display_person_data" , "display_picture"]
    can_delete = True
    verbose_name_plural = "FitnessAssessment"
    extra = 0
    classes = ["wide"]
class AbsenceTabular(admin.TabularInline) : 
    per_page = 15
    # template = 'admin/edit_inline/tabuler_with_paginator.html'
    model = Absence
    # fields = ["topic" ]
    # form = OrganizationTopicsForm
    # readonly_fields = [ "display_person_data" , "display_picture"]
    can_delete = True
    verbose_name_plural = "Absence"
    extra = 0
    classes = ["wide"]
class MuscleInformationTabular(admin.TabularInline) : 
    per_page = 15
    # template = 'admin/edit_inline/tabuler_with_paginator.html'
    model = MuscleInformation
    # fields = ["topic" ]
    # form = OrganizationTopicsForm
    # readonly_fields = [ "display_person_data" , "display_picture"]
    can_delete = True
    verbose_name_plural = "MuscleInformation"
    extra = 0
    classes = ["wide"]
    
@admin.register(Client)
class ClientAdmin(CustomModelAdmin):
    list_display = ('name', 'home_phone', 'address', 'occupation', 'date_of_birth', 'work_phone',  'day_number')
    search_fields = ('name', 'home_phone')
    inlines = (EmergencyContactTabular , MuscleInformationTabular , HealthHistoryTabular , MedicalInformationTabular , FitnessAssessmentTabular  )

@admin.register(EmergencyContact)
class EmergencyContactAdmin(CustomModelAdmin):
    list_display = ('client', 'name', 'phone', 'relationship')
    search_fields = ('client__name', 'name', 'phone')

@admin.register(MedicalInformation)
class MedicalInformationAdmin(CustomModelAdmin):
    list_display = ('client', 'physician', 'physician_phone', 'under_care', 'taking_medication', 'high_blood_pressure', 'bone_joint_problem', 'vigorous_exercise', 'chest_pain')
    search_fields = ('client__name', 'physician')

@admin.register(HealthHistory)
class HealthHistoryAdmin(CustomModelAdmin):
    list_display = ('client', 'asthma', 'respiratory_conditions', 'diabetes', 'epilepsy', 'osteoporosis')
    search_fields = ('client__name',)

@admin.register(FitnessAssessment)
class FitnessAssessmentAdmin(CustomModelAdmin):
    list_display = ('client', 'date', 'blood_pressure', 'resting_heart_rate', 'high_estimate_heart_rate', 'cardiovascular_test_name', 'cardiovascular_test_result')
    search_fields = ('client__name', 'cardiovascular_test_name')

@admin.register(TrainingPlan)
class TrainingPlanAdmin(CustomModelAdmin):
    list_display = ('client', 'level', 'frequency', 'date', 'created_by', 'updated_by')
    search_fields = ('client__name', 'level')

@admin.register(Exercise)
class ExerciseAdmin(CustomModelAdmin):
    list_display = ('training_plan', 'day', 'exercise_name', 'reps', 'sets', 'rest', 'created_by', 'updated_by')
    search_fields = ('training_plan__client__name', 'exercise_name')

@admin.register(Absence)
class AbsenceAdmin(CustomModelAdmin):
    list_display = ('client', 'date', 'reason')
    search_fields = ('client__name',)

@admin.register(MuscleInformation)
class MuscleInformationAdmin(CustomModelAdmin):
    list_display = ('client', 'muscle_group', 'size', 'date')
    search_fields = ('client__name', 'muscle_group')

@admin.register(ClientImage)
class ClientImageAdmin(CustomModelAdmin):
    list_display = ('client', 'image_path', 'date')
    search_fields = ('client__name',)
# from authen.models import User    
# admin.site.register(User)