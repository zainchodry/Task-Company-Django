from django.urls import path
from . views import *
from django.contrib.auth import views as auth_view
from . forms import *

urlpatterns = [
    path('dashboard',dashboard, name='dashboard'),
    path('project/new/',project_create, name = 'project_create'),
    path('project/<int:pk>',project_detail, name='project_detail'),
    path('task/new/', task_create, name='task_create'),
    path('report/new/',report_create, name='report_create'),
    path('', signup.as_view(), name = 'signup'),
    path('login', auth_view.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login')
]
