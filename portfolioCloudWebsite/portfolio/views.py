from django.shortcuts import render
from .models import WorkExperience, PersonalInfo

# Create your views here.
def home(request):
    work_exp = fetchWorkExperience()
    personal_info = fetchPersonalInfo()
    context = {
        'work_exp': work_exp,
        'personal_info': personal_info
    }
    return render(request, 'index.html', context=context)


def fetchWorkExperience():
    num_jobs = WorkExperience.objects.all().count()
    work_objects = WorkExperience.objects.all()
    work_exp = {
        'num_jobs': num_jobs,
        'work_objects': work_objects
    }
    return work_exp

def fetchPersonalInfo():
    personal_info = PersonalInfo.objects.first()
    return personal_info
