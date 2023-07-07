from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse
# Create your views here.
from faker import Faker
from random import randint
def fackerView(request):
    fack= Faker()
    roll=randint(1,20)
    fname=fack.first_name()
    lname=fack.last_name()
    email=fack.email()
    phone_no=fack.phone_number()

    s=Student(roll=roll,first_name=fname,last_name=lname,email=email,phone_number=phone_no)
    s.save()
    return HttpResponse("data saved")
def DisplayView(request):
    obj=Student.objects.all()
    temp_name='app1/show.html'
    context={'obj':obj}
    return render(request,temp_name,context)

def UpdateView(request,f_roll):
    temp_name="app1/update.html"
    obj=Student.objects.get(roll=f_roll)
    if request.method=='POST':
        obj.roll=request.POST.get('roll')
        obj.first_name=request.POST.get('first_name')
        obj.last_name=request.POST.get('last_name')
        obj.email=request.POST.get('email')
        obj.phone_number=request.POST.get('phone_number')

        obj.save()
        return redirect('show')


    context={'obj':obj}
    return render(request, temp_name, context)
def DeleteView(request,f_roll):
    temp_name="app1/confrim.html"
    obj1=Student.objects.get(roll=f_roll)
    if request.method =='POST':
        obj1.delete()
        return redirect ('show')
    context={'obj1':obj1}
    return render(request,temp_name,context)
def mul_chk(request):
    if request.method=='POST':
        obj1 = request.POST.getlist("chk")
        for i in obj1:
            m=Student.objects.get(roll=int(i))
            m.delete()
        return redirect ('show')
    return redirect('show')
