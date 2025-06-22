from django import forms
from .models import Project, Task, Report
from django.forms import TextInput, Textarea, Select, DateInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'lead']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter project description'}),
            'lead': Select(attrs={'class': 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'assigned_to', 'due_date']
        widgets = {
            'project': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}),
            'assigned_to': Select(attrs={'class': 'form-control'}),
            'due_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['task', 'content']
        widgets = {
            'task': Select(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your daily report'}),
        }



class signupForm(UserCreationForm):
    username = forms.CharField(label = 'Name', widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm-Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Pasword', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
            self.cleaned_data['username'] = user.username

        except:
            raise forms.ValidationError("Invalid Email Or PAssword")
        
        return super().clean()