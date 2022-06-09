from urllib import request
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, render
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def InsertPageView(request):
    return render(request, 'insert.html')

def InsertData(request):
    # Data from HTML to View
    edu_name = request.POST.get('edu_name')
    edu_major = request.POST.get('edu_major')
    edu_exp = request.POST.get('edu_exp')
    edu_course_1 = request.POST.get('edu_course_1')
    edu_course_2 = request.POST.get('edu_course_2')
    #edu_details = request.POST['edu_details']

    # Creating Object of Model Class

    # Inserting Data into a Table
    newuser = Educator.objects.create(edu_name=edu_name, edu_major=edu_major, edu_exp=edu_exp, edu_course_1=edu_course_1, edu_course_2=edu_course_2)
    #newuser.save()
    print(edu_name)
    print(edu_major)
    print(edu_exp)
    print(edu_course_1)
    print(edu_course_2)

    # After Insert render on show.html
    return redirect('show')

# Shpw Page View
def ShowPage(request):
    #SELECT * FROM table_name;
    all_data = Educator.objects.all()

    return render(request, 'show.html',{'key1': all_data})


# Update Page
def UpdatePage(request, pk):
    get_data = Educator.objects.get(id=pk)
    return render(request,'update.html',{'key2': get_data})

    #return render(request, 'edu_form.html')

# Update Data View
def UpdateData(request, pk):
    update_data = Educator.objects.get(id=pk)
    update_data.edu_name = request.POST['edu_name']
    update_data.edu_major = request.POST['edu_major']
    update_data.edu_exp = request.POST['edu_exp']
    update_data.edu_course_1 = request.POST['edu_course_1']
    update_data.edu_course_2 = request.POST['edu_course_2']

    # Query for Update
    update_data.save()

    # Showing a Updated Data
    return redirect('show')

# Delete Data View
def DeleteData(request, pk):
    delete_data = Educator.objects.get(id=pk)

    #Query for Delete 
    delete_data.delete()

    # Showing a Updated Data
    return redirect('show')