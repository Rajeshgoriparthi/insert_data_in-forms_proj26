from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
from app.forms import *

def dept(request):
    Lod=department.objects.all()
    d={'ddata':Lod}
    if request.method=='POST':
        did=request.POST['id']
        dname=request.POST['dname']
        loc=request.POST['loc']
        Do=department.objects.get_or_create(did=did,dname=dname,loc=loc)[0]
        Do.save()
        return render(request,'retrivedata_dept.html',d)
    return render(request,'dept.html')


def emp(request):
    Loe=employee.objects.all()
    d={'edata':Loe}
    if request.method=='POST':
        eid=request.POST['eid']
        ename=request.POST['ename']
        job=request.POST['job']
        sal=request.POST['sal']
        did=request.POST['did']
        Do=department.objects.get_or_create(did=did)[0]
        Eo=employee.objects.get_or_create(eid=eid,ename=ename,job=job,sal=sal,did=Do)[0]
        Eo.save()
        return render(request,'retrivedata_emp.html',d)
    return render(request,'emp.html')


# def retrivedata_dept(request):
#     Lod=department.objects.all()
#     d={'ddata':Lod}
#     return render(request,'retrivedata_dept.html',d)

# def retrivedata_emp(request):
#     Loe=employee.objects.all()
#     d={'edata':Loe}
#     return render(request,'retrivedata_emp.html',d)


def student_form(request):
    sfo=StudentForm()
    d={'sfo':sfo}
    if request.method=='POST':
        fd=StudentForm(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))
    return render(request,'student_form.html',d)