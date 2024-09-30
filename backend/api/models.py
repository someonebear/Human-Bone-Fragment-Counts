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


class Spit(models.Model):
    number = models.PositiveSmallIntegerField()
    site = models.ForeignKey(Site, related_name='spits',
                             on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.site.name}, {self.site.city} - Spit {self.number}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['number', 'site'], name='unique_site'),
        ]


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


class Individual(models.Model):
    ind_code = models.CharField(max_length=100, unique=True)
    meta = models.ForeignKey(
        'EntryMeta', related_name='individual', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.ind_code}'


class BodyPart(models.Model):
    bp_code = models.CharField(max_length=100, unique=True)
    ind = models.ForeignKey(
        Individual, related_name='body_parts', to_field='ind_code', on_delete=models.RESTRICT, blank=True, null=True)
    meta = models.ForeignKey(
        'EntryMeta', related_name='body_parts', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.bp_code}'


class EntryMeta(models.Model):
    class Sex(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        AMBIGUOUS = "Ambiguous"
        NOT_ASSESSED = "Not Assessed"

    class Age(models.TextChoices):
        INFANT = "Infant"
        CHILD = "Child"
        ADOLESCENT = "Adolescent"
        ADULT = "Adult"
        MAT_ADULT = "Mature Adult", "Mature Adult"
        NA = "Not Assessed", "Not Assessed"

    class Type(models.TextChoices):
        IND = "Individual", "Individual"
        BP = "Body Part", "Body Part"
        FRAG = "Fragment", "Fragment"

    sex = models.CharField(choices=Sex, max_length=50)
    site = models.ForeignKey(
        Site, related_name='site_entries', on_delete=models.RESTRICT)
    spit = models.ForeignKey(
        Spit, related_name='spit_entries', on_delete=models.RESTRICT)
    age = models.CharField(choices=Age, max_length=50)

    def __str__(self):
        return f'Meta {self.pk}, {self.spit.site.name} - Spit {self.spit.number}'


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

    body_part = models.ForeignKey(
        BodyPart, related_name='fragments', to_field='bp_code', on_delete=models.RESTRICT, blank=True, null=True)
    meta = models.ForeignKey(
        EntryMeta, related_name='fragments', on_delete=models.RESTRICT)
    # TODO regex validator for this acc_num field
    acc_num = models.CharField(max_length=100, unique=True)
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

    def __str__(self):
        return f'{self.acc_num}'

    class Meta:
        verbose_name_plural = "entries"
