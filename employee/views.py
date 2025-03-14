from django.shortcuts import render,  get_object_or_404
from .models import Employee, Project


def home(request):
    return render(request, 'home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html', {'emp' : employees})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'pro': projects})

def employee_detail(request, emp_id):
    employee = get_object_or_404(Employee, employee_id=emp_id)
    return render(request, 'employee_detail.html', {'emp': employee})

def project_detail(request, pro_id):
    project = get_object_or_404(Project, project_id=pro_id)
    employees = project.employees.all()
    return render(request, 'project_detail.html', {'pro': project, 'emp': employees})