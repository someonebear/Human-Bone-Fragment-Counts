from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=90)
    country = models.CharField(max_length=30)
    description = models.CharField(max_length=2000, blank=True)

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


class EntryGroup(models.Model):
    class Sex(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        AMBIGUOUS = "Ambiguous"
        NOT_ASSESSED = "Not Assessed"

    class Age(models.TextChoices):
        INFANT = "Infant"
        CHILD = "Child"
        ADOLESCENT = "Adolescent"
        YOUNG_ADULT = "Young Adult"
        ADULT = "Adult"
        MAT_ADULT = "Mature Adult", "Mature Adult"
        NA = "Not Applicable", "Not Applicable"

    class Type(models.TextChoices):
        IND = "Individual", "Individual"
        BP = "Body Part", "Body Part"
        FRAG = "Fragment", "Fragment"

    acc_num = models.CharField(max_length=100, unique=True)
    sex = models.CharField(choices=Sex, max_length=50)
    # site = models.ForeignKey(
    #     Site, related_name='site_entries', on_delete=models.RESTRICT)
    # spit = models.ForeignKey(
    #     Spit, related_name='spit_entries', on_delete=models.RESTRICT)
    age = models.CharField(choices=Age, max_length=50)
    entry_type = models.CharField(choices=Type, max_length=50)


class Entry(models.Model):
    class Side(models.TextChoices):
        LEFT = "Left"
        RIGHT = "Right"
        UNSIDED = "Unsided"

    class Size(models.TextChoices):
        CM_2 = "<2cm", "<2cm"
        CM_2_5 = "2-5cm", "2-5cm"
        CM_5_10 = "5-10cm", "5-10cm"
        CM_10 = ">10cm", ">10cm"

    # TODO regex validator for this acc_num fieldR
    acc_num = models.ForeignKey(
        EntryGroup, to_field='acc_num', max_length=50, on_delete=models.RESTRICT)
    bone = models.ForeignKey(Element, on_delete=models.RESTRICT)
    # TODO Add default as unsided
    side = models.CharField(choices=Side, max_length=20)
    size = models.CharField(choices=Size, max_length=50)
    generic = models.BooleanField(default=False)
    complete = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    notes = models.TextField(max_length=2000, blank=True)

    landmarks = models.ManyToManyField(Landmark)
    # logged_by = models.ForeignKey(User, on_delete=models.RESTRICT)    # TODO
    # TODO thumbnail

    class Meta:
        verbose_name_plural = "entries"
