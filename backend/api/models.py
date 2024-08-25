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
    city = models.CharField(max_length=90)
    country = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    
class Element(models.Model):
    bone_name = models.CharField(max_length=20)
    # bone_img = models.ImageField(upload_to='boneImages')
    
class Landmark(models.Model):
    landmark_name = models.CharField(max_length=100)
    bone = models.ForeignKey(Element, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.landmark_name
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
        
    site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    logged_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    bone = models.ForeignKey(Element, on_delete=models.RESTRICT)
    side = models.CharField(choices=Side, max_length=20)
    age = models.CharField(choices=Age, max_length=50)
    sex = models.CharField(choices=Sex, max_length=50)
    size = models.CharField(choices=Size, max_length=50)
    generic = models.BooleanField()
    complete = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    notes = models.CharField(max_length=2000)
    
    landmarks = models.ManyToManyField(Landmark, through="IDLandmarks")

class IDLandmarks(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.RESTRICT)
    landmark = models.ForeignKey(Landmark, on_delete=models.RESTRICT)
    found = models.BooleanField(default=False)