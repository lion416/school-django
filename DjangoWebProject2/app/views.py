"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import accountInfo

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def signup(request):
    """Renders the signup page."""

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup.html',
        {
            'title':'Signup',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def signup_student(request):
    "Renders the login page."
    student_name = request.POST["student_name"]
    student_password = request.POST["student_password"]
    student_info = accountInfo(student_name = student_name, student_password = student_password)
    student_info.save()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Signup',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def signup_teacher(request):
    """Renders the signup_teacher page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup_teacher.html',
        {
            'title':'Signup_teacher',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
