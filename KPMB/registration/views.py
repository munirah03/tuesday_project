from django.shortcuts import render
from registration.models import Course
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    context = {
        'firstname' : 'Puteri Nurul Haziqah',
        'age' : '22'
    }
    return render(request, "index.html", context)

def new_course(request):

    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']

        data = Course(code=c_code, desc=c_desc)
        data.save()
        dict={
            'message':'Data Saved'
        }
        return render (request, 'new_course.html', dict)
    else:
        dict = {
            'message':' '
        }
        return render(request,'new_course.html')
    
def course(request):
    
    alldata=Course.objects.all()
    dict={
        'alldata':alldata
    }
    return render(request,'course.html',dict)

def update(request, code):
    data = Course.objects.get(code=code)
    dict ={
        'data':data
    }
    return render(request, "update.html",dict)

def update_data(request, code):
    desc = request.POST['desc']
    data = Course.objects.get(code=code) 
    data.desc=desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def searchpage(request):

    members = Course.objects.filter(Q(code=request.GET.get('search')))
    return render(request, 'searchpage.html', {'members': members})