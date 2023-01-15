from django.shortcuts import render,redirect
from .models import Departments,Doctors
from django.http import HttpResponse


def departments(request):
    department = Departments.objects.all()
    context = {
        "departments":department
    }
    return render(request,"vending_machine/departments.html",context)

def doctors(request):
    if request.method == "POST":
        choosen_department = request.POST['department']
        doctors = Doctors.objects.filter(department__name__icontains=str(choosen_department))
        context = {
            "doctors" : doctors,
        }
        return render(request,"vending_machine/doctors.html",context)
    else:
        return redirect("doctors")

def token(request):
    if request.method =="POST":
        choosen_doctor = request.POST['doctor']
        confirm_doctor = Doctors.objects.get(serial_no__iexact = choosen_doctor)
        tokens = confirm_doctor.tokens
        context = {
            "doctor" : confirm_doctor,
        }
        return render(request,"vending_machine/token.html",context)

def token_generation(request):
    if request.method == "POST":
        choosen_doctor = request.POST['doctor_id']
        confirm_doctor = Doctors.objects.get(id__iexact=choosen_doctor)
        doctor_name = confirm_doctor.first_name +" " +confirm_doctor.last_name
        department_name = confirm_doctor.department.name[2:]
        token_dep = confirm_doctor.department.name[-2:-3:-1]
        token_doctor = confirm_doctor.first_name[:1] + confirm_doctor.last_name[:1]
        tokens_num = confirm_doctor.tokens
        if tokens_num == "":
            tokens_num = 1
        else:
            list_tokens = confirm_doctor.tokens.split(",")
            tot_tokens = len(list_tokens)
            tokens_num = str(tot_tokens)
        token_generate = token_dep + "-" + token_doctor + "-" + str(tokens_num)
        confirm_doctor.tokens += (token_generate + ",")
        confirm_doctor.save()

        context = {
            "doctor_name" : doctor_name,
            "department_name" : department_name,
            "doctor" : confirm_doctor,
            "token" : token_generate,
        }

        return render(request,"vending_machine/token_generation.html",context)