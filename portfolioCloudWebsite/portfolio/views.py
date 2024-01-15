from django.shortcuts import render
from .models import WorkExperience, PersonalInfo, Skill, Project

# Create your views here.
def home(request):
    work_exp = fetchWorkExperience()
    personal_info = fetchPersonalInfo()
    fetch_skills = fetchSkills()
    projects = fetchProjects()
    context = {
        'work_exp': work_exp,
        'personal_info': personal_info,
        'skill_info': fetch_skills,
        'projects': projects
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

def fetchSkills():
    num_skills = Skill.objects.all().count()
    skills = Skill.objects.all()
    skill_info = {
        'num_skills': num_skills,
        'skills': skills
    }
    return skill_info

def fetchProjects():
    project_objects = Project.objects.all()
    return project_objects

