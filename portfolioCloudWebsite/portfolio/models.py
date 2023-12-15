from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    LEVELS= (
        ('b', 'Beginner'),
        ('i', 'Intermediate'),
        ('a', 'Advanced')
    )

    level = models.CharField(
        max_length = 1,
        choices=LEVELS,
        default='b'
    )

    TYPES = (
        ('p', 'Programming Languages'),
        ('d', 'Databases'),
        ('f', 'Frameworks and Tools'),
        ('w', 'Web Technologies')
    )

    type = models.CharField(
        max_length = 1,
        choices=TYPES,
    )

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    achievements = models.TextField()
    github = models.CharField(max_length=100, blank=True)

class Education(models.Model):
    id = models.IntegerField(primary_key=True)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    courses = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    acquired_GPA = models.DecimalField(max_digits=10, decimal_places=2)
    out_of_GPA = models.DecimalField(max_digits=10, decimal_places=2)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)

class WorkExperience(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # <!-- your_template.html -->
    # {{ your_model_instance.your_date_field|date:"F Y" }}
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    achievements = models.TextField()

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    age = models.IntegerField()
    career_obj = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    date_acquired = models.CharField(max_length=100)