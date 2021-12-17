from rest_framework import serializers

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
WORK_TYPE = (
    ('Private', 'Private'),
    ('Self-employed', 'Self-employed'),
)
RESIDENCE_TYPE = (
    ('Urban', 'Urban'),
    ('Rural', 'Rural'),
)
BOOL_CHOICES = (
    (0, 0),
    (1, 1)
)
SMOKING_TYPE = (
    ('formerly smoked', 'formerly smoked'),
    ('never smoked', 'never smoked'),
    ('smokes', 'smokes'),
    ('Unknown', 'Unknown')
)


class PredictionSerializer(serializers.Serializer):
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    age = serializers.IntegerField()
    hypertension = serializers.ChoiceField(choices=BOOL_CHOICES)
    heart_disease = serializers.ChoiceField(choices=BOOL_CHOICES)
    ever_married = serializers.ChoiceField(choices=BOOL_CHOICES)
    work_type = serializers.ChoiceField(choices=WORK_TYPE)
    residence_type = serializers.ChoiceField(
        choices=RESIDENCE_TYPE)
    avg_glucose_level = serializers.FloatField()
    bmi = serializers.IntegerField()
    smoking_status = serializers.ChoiceField(
        choices=SMOKING_TYPE)
