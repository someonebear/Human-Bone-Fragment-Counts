from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=320)
    role = models.CharField(max_length=50)
    
class Site(models.Model):
    site_name = models.CharField(max_length=100)
    city = models.charField(max_length=90)
    country = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    
class Elements(models.Model):
    bone_name = models.CharField(max_length=20)
    bone_img = models.ImageField(upload_to='boneImages')
    
class Landmarks(models.Model):
    landmark_name = models.CharField(max_length=100)
    bone = models.ForeignKey(Elements)
    
    
# note: still have to add spit/accno/person IDs
# spit may have to be another model

class Entry(models.Model):
    class Side(models.TextChoices):
        LEFT = "Left"
        RIGHT = "Right"
        UNSIDED = "Unsided"
    class Age(models.TextChoices):
        INFANT = "Infant"
        CHILD = "Child"
        ADOLESCENT = "Adolescent"
        SKEL_MAT = "Skeletally Mature"
        MAT_AD = "Mature Adult"
    class Sex(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        AMBIGUOUS = "Ambiguous"
        NOT_ASSESS = "Not Assessed"
    class Size(models.TextChoices):
        CM_2 = "< 2cm"
        CM_2_5  = "2-5cm"
        CM_5_10 = "2-10cm"
        CM_10 = ">10cm"
        
    site = models.ForeignKey(Site)
    logged_by = models.ForeignKey(User)
    bone = models.ForeignKey(Elements)
    side = models.CharField(choices=Side)
    age = models.CharField(choices=Age)
    sex = models.CharField(choices=Sex)
    size = models.CharField(choices=Size)
    generic = models.BooleanField()
    complete = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    notes = models.CharField(max_length=2000)