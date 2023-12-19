from django.shortcuts import render
from .models import WorkExperience

# Create your views here.
def home(request):
    num_jobs = WorkExperience.objects.all().count()
    work_objects = WorkExperience.objects.all()
    context = {
        'num_jobs': num_jobs,
        'work_objects': work_objects
    }
    return render(request, 'index.html', context=context)


def fetchWorkExperience():
    num_jobs = WorkExperience.objects.all().count()
