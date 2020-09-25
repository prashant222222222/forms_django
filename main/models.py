from django.db import models

# Create your models here.
#model form
class Student(models.Model):
    GENDERS=(
    ('F','FEMALE'),
    ('M','MALE')
    )
    name=models.CharField(max_length=256)
    roll_number=models.IntegerField()
    gender=models.CharField(max_length=1,choices=GENDERS)
