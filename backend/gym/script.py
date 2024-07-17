# python manage.py shell < script.py


from django.utils import timezone
from django.core.management import call_command
from authen.models import User
from client.models import (
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
import random

# Create users
created_by_user = User.objects.get(id=1)
updated_by_user = User.objects.get(id=1)

# Create clients
client1 = Client.objects.create(
    name='Abdelfattah',
    home_phone='+201001234567',
    address='123 Main St',
    occupation='Engineer',
    date_of_birth='1990-01-01',
    id_number='1234567890',
    work_phone='+201001234568',
    date_joined=timezone.now().date(),
    created_by=created_by_user,
    updated_by=updated_by_user,
    day_number=1
)

client2 = Client.objects.create(
    name='Khattab',
    home_phone='+201001234569',
    address='456 Elm St',
    occupation='Doctor',
    date_of_birth='1985-05-05',
    id_number='0987654321',
    work_phone='+201001234570',
    date_joined=timezone.now().date(),
    created_by=created_by_user,
    updated_by=updated_by_user,
    day_number=2
)

# Create emergency contacts
EmergencyContact.objects.create(
    client=client1,
    name='Ahmed Ali',
    phone='+201001234571',
    relationship='Brother'
)

EmergencyContact.objects.create(
    client=client2,
    name='Sara Mohamed',
    phone='+201001234572',
    relationship='Sister'
)

# Create medical information
MedicalInformation.objects.create(
    client=client1,
    physician='Dr. Smith',
    physician_phone='+201001234573',
    under_care=True,
    care_reason='Hypertension',
    taking_medication=True,
    medication_list='Lisinopril',
    allergies='Peanuts',
    high_blood_pressure=True,
    bone_joint_problem=False,
    vigorous_exercise=True,
    chest_pain=False,
    smoking_habits='Non-smoker',
    family_history={'heart_disease': True, 'diabetes': False},
    lifestyle_factors={'diet': 'Vegetarian', 'exercise': 'Regular'},
    cardiovascular_conditions={'heart_attack': False, 'stroke': False},
    work_exercise_habits={'office_work': True, 'manual_labor': False},
    nutritional_info={'caloric_intake': '2000', 'supplements': 'None'}
)

MedicalInformation.objects.create(
    client=client2,
    physician='Dr. Johnson',
    physician_phone='+201001234574',
    under_care=False,
    taking_medication=False,
    high_blood_pressure=False,
    bone_joint_problem=True,
    vigorous_exercise=False,
    chest_pain=True,
    smoking_habits='Smoker',
    family_history={'heart_disease': False, 'diabetes': True},
    lifestyle_factors={'diet': 'Non-vegetarian', 'exercise': 'Irregular'},
    cardiovascular_conditions={'heart_attack': True, 'stroke': False},
    work_exercise_habits={'office_work': False, 'manual_labor': True},
    nutritional_info={'caloric_intake': '2500', 'supplements': 'Vitamins'}
)

# Create health history
HealthHistory.objects.create(
    client=client1,
    asthma={'present': False},
    respiratory_conditions={'bronchitis': False},
    diabetes={'type1': False, 'type2': False},
    epilepsy={'seizures': False},
    osteoporosis={'bone_density': 'Normal'},
    other_conditions={'thyroid_issues': False}
)

HealthHistory.objects.create(
    client=client2,
    asthma={'present': True},
    respiratory_conditions={'bronchitis': True},
    diabetes={'type1': False, 'type2': True},
    epilepsy={'seizures': True},
    osteoporosis={'bone_density': 'Low'},
    other_conditions={'thyroid_issues': True}
)

# Create fitness assessments
FitnessAssessment.objects.create(
    client=client1,
    date=timezone.now().date(),
    blood_pressure='120/80',
    resting_heart_rate='70',
    high_estimate_heart_rate='180',
    cardiovascular_test_name='Treadmill Test',
    cardiovascular_test_result='Good',
    muscle_strength_bench_press='50kg',
    muscle_strength_leg_press='100kg',
    muscle_strength_advanced_1rm='75kg',
    flexibility_zipper_stretch='Good',
    flexibility_sit_and_reach='Average',
    push_ups='20',
    sit_ups='30',
    walk_test='Passed'
)

FitnessAssessment.objects.create(
    client=client2,
    date=timezone.now().date(),
    blood_pressure='130/85',
    resting_heart_rate='75',
    high_estimate_heart_rate='170',
    cardiovascular_test_name='Cycling Test',
    cardiovascular_test_result='Average',
    muscle_strength_bench_press='60kg',
    muscle_strength_leg_press='110kg',
    muscle_strength_advanced_1rm='80kg',
    flexibility_zipper_stretch='Average',
    flexibility_sit_and_reach='Good',
    push_ups='25',
    sit_ups='35',
    walk_test='Passed'
)

# Create training plans
training_plan1 = TrainingPlan.objects.create(
    client=client1,
    level='Beginner',
    frequency=3,
    program='Full Body Workout',
    date=timezone.now().date(),
    created_by=created_by_user,
    updated_by=updated_by_user
)

training_plan2 = TrainingPlan.objects.create(
    client=client2,
    level='Intermediate',
    frequency=5,
    program='Cardio and Strength Training',
    date=timezone.now().date(),
    created_by=created_by_user,
    updated_by=updated_by_user
)

# Create exercises
Exercise.objects.create(
    training_plan=training_plan1,
    day='Monday',
    exercise_name='Push Ups',
    reps=10,
    sets=3,
    rest=60,
    created_by=created_by_user,
    updated_by=updated_by_user
)

Exercise.objects.create(
    training_plan=training_plan2,
    day='Tuesday',
    exercise_name='Bench Press',
    reps=8,
    sets=4,
    rest=90,
    created_by=created_by_user,
    updated_by=updated_by_user
)

# Create absences
Absence.objects.create(
    client=client1,
    date=timezone.now().date(),
    reason='Medical Appointment'
)

Absence.objects.create(
    client=client2,
    date=timezone.now().date(),
    reason='Family Event'
)

# Create muscle information
from django.utils import timezone
from .models import Client, MuscleInformation

# Assuming 'client1' and 'client2' are instances of Client model for Abdelfattah and Khattab respectively

# For client1 (Abdelfattah)
MuscleInformation.objects.create(
    client=client1,
    muscle_group='BACK',
    size='Large',
    comments='Good progress in upper back muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='SHOULDER',
    size='Medium',
    comments='Steady improvement in shoulder muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='ARM',
    size='Medium',
    comments='Consistent strength in arm muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='HAND',
    size='Small',
    comments='Working on wrist and hand flexibility',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='LOWER_BACK',
    size='Medium',
    comments='Improving lower back strength',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='HIP',
    size='Large',
    comments='Strong hip and pelvis muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='KNEE',
    size='Medium',
    comments='Stable thigh and knee muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client1,
    muscle_group='ARTHRITIS',
    size='Small',
    comments='Managing arthritis symptoms',
    date=timezone.now().date()
)

# For client2 (Khattab)
MuscleInformation.objects.create(
    client=client2,
    muscle_group='BACK',
    size='Medium',
    comments='Needs more work on upper back muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='SHOULDER',
    size='Small',
    comments='Developing shoulder muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='ARM',
    size='Medium',
    comments='Improving arm strength',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='HAND',
    size='Small',
    comments='Focusing on hand dexterity exercises',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='LOWER_BACK',
    size='Small',
    comments='Addressing lower back pain',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='HIP',
    size='Medium',
    comments='Working on hip flexibility and strength',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='KNEE',
    size='Large',
    comments='Strong thigh and knee muscles',
    date=timezone.now().date()
)

MuscleInformation.objects.create(
    client=client2,
    muscle_group='ARTHRITIS',
    size='Medium',
    comments='Managing arthritis symptoms',
    date=timezone.now().date()
)

# Create client images
ClientImage.objects.create(
    client=client1,
    image_path='client_images/abdelfattah.jpg',
    date=timezone.now().date()
)

ClientImage.objects.create(
    client=client2,
    image_path='client_images/khattab.jpg',
    date=timezone.now().date()
)
