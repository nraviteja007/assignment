from django.shortcuts import render,redirect
from vending_machine.models import Departments,Doctors


def home(request):
    department = Departments.objects.all()
    context = {
        "departments":department,
    }
    return render(request,"doctor_app/home_doctors_departments.html",context)


def doctors_view(request):
    if request.method == "POST":
        choosen_department = request.POST['department']
        doctors = Doctors.objects.filter(department__name__icontains=str(choosen_department))
        context = {
            "doctors" : doctors,
        }
        return render(request,"doctor_app/doctors_doctor_details.html",context)
    else:
        return redirect("doctors_view")

def doctor_loggedin(request):
    if  request.method == "POST":
        choosen_doctor = request.POST['doctor']
        confirm_doctor = Doctors.objects.get(serial_no__iexact=choosen_doctor)
        doctor_name = confirm_doctor.first_name + " "+confirm_doctor.last_name
        tokens = confirm_doctor.tokens
        current_token = confirm_doctor.current_token
        next_token = confirm_doctor.next_token
        total_tokens = len(tokens.split(","))
        context = {
            "doctor_obj" : confirm_doctor,
            "doctor_name" : doctor_name,
            "tokens" : tokens,
            "current_token": current_token,
            "next_token": next_token,
            "total_tokens" : total_tokens-1,
        }
        return render(request,"doctor_app/doctor_loggedin.html",context)
    else:
        return redirect("home_doc")
def current_token(request,doctor_id):
    confirm_doctor = Doctors.objects.get(id=doctor_id)
    doctor_name = confirm_doctor.first_name + " " + confirm_doctor.last_name
    tokens = confirm_doctor.tokens
    token_list = tokens.split(",")
    if len(token_list) > 0:
        current_token = token_list[0]
    confirm_doctor.current_token = current_token
    confirm_doctor.next_token = ""
    confirm_doctor.save()
    total_tokens = len(token_list)
    context = {
        "doctor_obj": confirm_doctor,
        "doctor_name": doctor_name,
        "tokens": tokens,
        "current_token":current_token,
        "next_token" : next_token,
        "total_tokens" : total_tokens-1,
    }
    return render(request,"doctor_app/doctor_loggedin.html",context)

def next_token(request,doctor_id,current_token):
    confirm_doctor = Doctors.objects.get(id=doctor_id)
    doctor_name = confirm_doctor.first_name + " " + confirm_doctor.last_name
    tokens = confirm_doctor.tokens
    list_tokens=confirm_doctor.tokens.split(",")
    current = list_tokens.index(current_token)
    confirm_doctor.current_token = list_tokens[current+1]
    confirm_doctor.next_token = list_tokens[current+2]
    confirm_doctor.save()
    current_token = confirm_doctor.current_token
    next_token = confirm_doctor.next_token
    total_tokens = len(tokens)
    context = {
        "doctor_obj": confirm_doctor,
        "doctor_name": doctor_name,
        "tokens": tokens,
        "current_token":current_token,
        "next_token" : next_token,
        "total_tokens" : total_tokens-1,
    }
    return render(request,"doctor_app/doctor_loggedin.html",context)


def reset_tokens(request,doctor_id):
        confirm_doctor = Doctors.objects.get(id=doctor_id)
        confirm_doctor.tokens = ""
        confirm_doctor.current_token = ""
        confirm_doctor.next_token = ""
        confirm_doctor.save()
        return redirect('home_doc')


