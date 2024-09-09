from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     email = models.EmailField(max_length=320)
#     role = models.CharField(max_length=50)


class Site(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=90)
    country = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.name} - {self.city}, {self.country}'


class Element(models.Model):
    name = models.CharField(max_length=50)
    # For big bones like the cranium with multiple parts and duplicate landmarks
    secondary = models.CharField(max_length=50, blank=True)

    def __str__(self):
        if self.secondary != "":
            return f'{self.name} - {self.secondary}'
        return self.name

    class Meta:
        models.UniqueConstraint(
            fields=['name', 'secondary'], name='unique_bone')
    # bone_img = models.ImageField(upload_to='boneImages')


class Landmark(models.Model):
    # e.g. FIB-1 for the head of the fibula
    landmark_id = models.CharField(max_length=20, unique=True)
    # Common name - e.g. "head", not "caput fibulae"
    name = models.CharField(max_length=100)
    bone = models.ForeignKey(
        Element, related_name='landmarks', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.landmark_id} - {self.name}'

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
        YOUNG_ADULT = "Young Adult"
        ADULT = "ADULT"
        MAT_ADULT = "Mature Adult", "Mature Adult"
        NA = "Not Applicable", "Not Applicable"

    class Sex(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        AMBIGUOUS = "Ambiguous"
        NOT_ASSESSED = "Not Assessed"

    class Size(models.TextChoices):
        CM_2 = "<2cm", "<2cm"
        CM_2_5 = "2-5cm", "2-5cm"
        CM_5_10 = "5-10cm", "5-10cm"
        CM_10 = ">10cm", ">10cm"

    # site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    # logged_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    # TODO regex validator for this acc_num field
    acc_num = models.CharField(max_length=50)
    bone = models.ForeignKey(Element, on_delete=models.RESTRICT)
    side = models.CharField(choices=Side, max_length=20)
    age = models.CharField(choices=Age, max_length=50)
    sex = models.CharField(choices=Sex, max_length=50)
    size = models.CharField(choices=Size, max_length=50)
    generic = models.BooleanField(default=False)
    complete = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    notes = models.TextField(max_length=2000, blank=True)

    # landmarks = models.ManyToManyField(Landmark, through="IDLandmarks")
    landmarks = models.ManyToManyField(Landmark)

    class Meta:
        verbose_name_plural = "entries"


# class IDLandmarks(models.Model):
#     entry = models.ForeignKey(Entry, on_delete=models.RESTRICT)
#     landmark = models.ForeignKey(Landmark, on_delete=models.RESTRICT)
#     found = models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural = "identified landmarks"
