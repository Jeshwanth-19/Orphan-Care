from django.shortcuts import render
from.models import Care
from.models import Details
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
#ceate your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        new_user = User.objects.create_user(
            username = username,
            password = password,
            first_name = first_name,
            last_name=last_name,
            email=email
        )
        new_user.save()
        return redirect('/signin/')
    form = SignupForm()
    return render(request, 'signup.html', {'form':form})
    
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request,'donor.html',{})
        else:
            return HttpResponse('No user found with the given credentials')
    return render(request, 'signin.html', {})


def signout(request):
    logout(request)
    return redirect('/signin/')
def Aboutus(request):
     return render(request, 'Aboutus.html')
def donor(request):
    return render(request, 'donor.html')
def services(request):
    return render(request,'services.html')
def addregistration(request):
    if request.method == "POST":
        new_care = Care.objects.create(
            Organizationname=request.POST['Organizationname'],
            Firstname=request.POST['Firstname'],
            Lastname=request.POST['Lastname'],
            Dateofbirth=request.POST['Dateofbirth'],
            Emailfield=request.POST['Emailfield'],
            Contactnumber=request.POST['Contactnumber'],
            Eadhar=request.POST['Eadhar'],
            Establish=request.POST['Establish'],
            Govtissueid=request.POST['Govtissueid'],
            Numberoforphans=request.POST['Numberoforphans'],
            Upi=request.POST['Upi'],
            Accountdetails=request.POST['Accountdetails'],
            Address=request.POST['Address'],
            Village=request.POST['Village'],
            District=request.POST['District'],
            State=request.POST['State'],
            Pincode=request.POST['Pincode'],
            Description=request.POST['Description']
            )
        new_care.save()
        return HttpResponse('''Thank you for registering!!!.
        We have recieved your details we will update you soon with a Call!!!''')
    return render(request, 'addregistration.html')

def all_list(request):
    details_list=Details.objects.all()
    return render(request,'details_list.html',{'details_list' : details_list})
