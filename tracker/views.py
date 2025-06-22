from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import *
from django.utils import timezone
from django.views import View
# Create your views here.







@login_required
def dashboard(request):
    if request.user == request.user:
        projects = Project.objects.filter(lead = request.user)
        tasks = Task.objects.filter(assigned_to = request.user)
        context = {
            'projects':projects,
            'tasks':tasks
        }
    return render(request, "dashboard.html",context)



@login_required
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, "form.html", {'form':form, 'title':'New Project'})



@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, "form.html", {'form':form, 'title':'New Task'})


@login_required
def report_create(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        report = form.save(commit=False)
        report.reporter = request.user
        report.save()
        task = report.task
        task.completed = True
        task.completed_at = timezone.now()
        task.save()
        return redirect('dashboard')
    return render(request,'tracker/form.html', {'form':form,'title':'Daily Report'})



@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()
    return render(request,'project_detail.html', {'project':project,'tasks':tasks})



class signup(View):
    def get(self,request):
        form = signupForm()
        context = {
            "form":form
        }
        return render(request,"signup.html", context)
    
    def post(self, request):
        if request.method == 'POST':
            form = signupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            form = signupForm()
        return render(request, "signup.html", {"form":form})
    
    
    
