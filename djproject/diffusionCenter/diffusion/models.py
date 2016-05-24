from django.db import models

# Create your models here.
class ContactProfile(models.Model):
    name = models.CharField(max_length=100)
    length_nm = models.IntegerField(default=50)
    profile = models.TextField()

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    RTA_TYPES = (
        ('F', 'Furnace'),
        ('L', 'Lamp'),
    )
    rta_type = models.CharField(max_length=1, choices=RTA_TYPES)
    treatment_times = models.TextField()

#decribes material in isolation
class Material(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    heat_transfer_coefficient = models.FloatField(default=0)
    thermal_conductivity = models.FloatField()
    melting_point = models.FloatField()
    additional_data = models.TextField() #A JSON (its fields may need to be later added to model)

#describes how different materials diffuse through one another
class DiffusionRelation(models.Model):
    DIFFUSION_TYPES = (
        ('INTER', 'Interdiffusion'),
        ('IMPUR', 'Impurity'),
        ('SELF', 'Self'),
    )
    diffusion_type = models.CharField(max_length=5, choices=DIFFUSION_TYPES)
    material_1 = models.CharField(max_length=10) #short_name of material in higher concentration
    material_2 = models.CharField(max_length=10) #short_name of material in lower concentration
    additional_data = models.TextField() #A JSON (its fields may need to be later added to model)

class AnnealRecord(models.Model):
    profile_name = models.CharField(max_length=50)
    treatment_name = models.CharField(max_length=100)
    data = models.TextField() #A JSON (its fields may need to be later added to model)
