from django.db import models
from gym.models import BaseModel
from authen.models import User
from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

def validate_non_negative(value):
    if value < 0:
        raise ValidationError('Value cannot be negative.')

class Client(BaseModel):
    name = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')
    ] , null=True)
    address = models.CharField(max_length=255 , null=True)
    occupation = models.CharField(max_length=100 , null=True)
    date_of_birth = models.DateField()
    # id_number = models.CharField(max_length=20, unique=True)
    work_phone = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')
    ] , null= True)
    # date_joined = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name="person" , null=True , blank=True)
    
    created_by = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , related_name="created_user")
    updated_by = models.ForeignKey(User , on_delete=models.SET_NULL , null= True , related_name="updated_user") 
    day_number = models.IntegerField(default=0)

class EmergencyContact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')
    ])
    relationship = models.CharField(max_length=50)

class MedicalInformation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='medical_information')
    physician = models.CharField(max_length=100)
    physician_phone = models.CharField(max_length=15, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')
    ])
    under_care = models.BooleanField()
    care_reason = models.TextField(blank=True, null=True)
    taking_medication = models.BooleanField()
    medication_list = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    high_blood_pressure = models.BooleanField()
    bone_joint_problem = models.BooleanField()
    vigorous_exercise = models.BooleanField()
    chest_pain = models.BooleanField()
    smoking_habits = models.TextField()
    family_history = models.JSONField()
    lifestyle_factors = models.JSONField()
    cardiovascular_conditions = models.JSONField()
    work_exercise_habits = models.JSONField()
    nutritional_info = models.JSONField()

class HealthHistory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='health_history')
    asthma = models.JSONField()
    respiratory_conditions = models.JSONField()
    diabetes = models.JSONField()
    epilepsy = models.JSONField()
    osteoporosis = models.JSONField()
    other_conditions = models.JSONField()

class FitnessAssessment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='fitness_assessments')
    date = models.DateField()
    blood_pressure = models.CharField(max_length=20)
    resting_heart_rate = models.CharField(max_length=20, validators=[validate_non_negative])
    high_estimate_heart_rate = models.CharField(max_length=20, validators=[validate_non_negative])
    cardiovascular_test_name = models.CharField(max_length=100)
    cardiovascular_test_result = models.CharField(max_length=100)
    muscle_strength_bench_press = models.CharField(max_length=100)
    muscle_strength_leg_press = models.CharField(max_length=100)
    muscle_strength_advanced_1rm = models.CharField(max_length=100)
    flexibility_zipper_stretch = models.CharField(max_length=100)
    flexibility_sit_and_reach = models.CharField(max_length=100)
    push_ups = models.CharField(max_length=100)
    sit_ups = models.CharField(max_length=100)
    walk_test = models.CharField(max_length=100)
    class Meta:
        # Ensure each combination of client, muscle_group, and date is unique
        unique_together = ['client', 'date']

class TrainingPlan(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='training_plans')
    level = models.CharField(max_length=50)
    frequency = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    program = models.TextField()
    date = models.DateField()
    created_by = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , related_name="created_training_plans")
    updated_by = models.ForeignKey(User , on_delete=models.SET_NULL , null= True , related_name="updated_training_plans") 
    

class Exercise(BaseModel):
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='exercises')
    day = models.CharField(max_length=20)
    exercise_name = models.CharField(max_length=100)
    reps = models.PositiveIntegerField(validators=[validate_non_negative])
    sets = models.PositiveIntegerField(validators=[validate_non_negative])
    rest = models.PositiveIntegerField(validators=[validate_non_negative])
    created_by = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , related_name="created_exercise")
    updated_by = models.ForeignKey(User , on_delete=models.SET_NULL , null= True , related_name="updated_exercise") 
    
    class Meta:
        # Ensure each combination of client, muscle_group, and date is unique
        unique_together = ['exercise_name', 'training_plan']
    

class Absence(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField()
    reason = models.TextField(blank=True, null=True)
    class Meta:
        # Ensure each combination of client, muscle_group, and date is unique
        unique_together = ['client', 'date']

class MuscleInformation(models.Model):
    muscles = ( 
        ("BACK", "Upper back"),
        ("SHOULDER", "Shoulder/clavicle"),
        ("ARM", "Arm/elbow"),
        ("HAND", "Wrist/hand"),
        ("LOWER_BACK", "Lower back"),
        ("HIP", "Hip/pelvis"),
        ("KNEE", "Thigh/Knee"),
        ("ARTHRITIS", "Arthritis"),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='muscle_information')
    muscle_group = models.CharField(max_length=100 , choices=muscles)
    size = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    date = models.DateField()
    class Meta:
        # Ensure each combination of client, muscle_group, and date is unique
        unique_together = ['client', 'muscle_group', 'date']
    

class ClientImage(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='images')
    image_path = models.ImageField(upload_to='client_images/')
    date = models.DateField()
    
