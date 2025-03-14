from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('', views.home, name='home'),

    path('employees/', views.employee_list, name="employee_list"),

    path('projects/', views.project_list, name="project_list"),

    path('employees/<int:emp_id>/', views.employee_detail, name='employee_detail'),
    
    path('projects/<int:pro_id>/', views.project_detail, name='project_detail'),
]
