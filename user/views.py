from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from user.models import Payments, Profile
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from user.complete_payment import CompletePayment


def mainpage(request):
    return redirect("./dashboard")

def signup(request):
    msgs = []
    it = True
    if request.method == "POST":
        try:
            b =(datetime.now() - datetime.strptime(str(request.POST["dob"]), "%Y-%m-%d")).days/365.2425
        except:
            it = False
            msgs.append("Enter valid dates only")
        if len(request.POST["name"]) == 0:
            it = False
            msgs.append("Please enter a valid name")
        elif len(request.POST["email"]) == 0:
            it = False
            msgs.append("Please enter a valid email address")
        elif len(request.POST["pass1"]) < 8 or request.POST["pass1"] != request.POST["pass2"]:
            it = False
            msgs.append("Password must contain 8 letters and must match with the confirm password")
        elif b < 18 or b > 65:
            it = False
            msgs.append("Age must be between 18 and 65")
        
        if it:
            use = User.objects.create(
                username = request.POST["name"],
                email = request.POST["email"]
            )
            use.set_password(request.POST["pass1"])
            pro = Profile.objects.create(
                user = use,
                dob = request.POST["dob"]
            )
            use.save()
            login(request,use)
            return redirect('../dashboard')
            
    return render(request,"user/signup.html",{"msgs":msgs})

def signin(request):
    msgs = []
    username = ''
    if request.method == 'POST':
        user = authenticate(request,username = request.POST['name'], password = request.POST["pass"])
        if user is not None:
            msgs.append("Logged in successfully with: "+request.POST['name'])
            login(request,user)
            return redirect('../dashboard')
        else:
            msgs.append("Invalid Credentials, please enter valid username and password")
            username = request.POST["name"]

    return render(request,"user/signin.html",{"msgs":msgs,"user":username})

def dashboard(request):
    if not request.user.is_authenticated: 
        return render(request,"user/dashboard.html")
    Payment_string = ""
    profile = Profile.objects.filter(user = request.user).first()
    if profile.last_date_of_payment == None or profile.last_date_of_payment == '':
        Payment_string = "No previous transaction details exist."
    else:
        Payment_string = "Last Transaction was on "+str(profile.last_date_of_payment.strftime("%d-%m-%Y"))
    slot = -1 
    try:
        difference = (datetime.now() - profile.last_date_of_payment.replace(tzinfo=None)).days
        if difference < 30:
            slot = profile.slot
    except:
        difference = 30
    return render(request,"user/dashboard.html",{"Payment_string":Payment_string,"slot":slot,"diff":max(0,30-difference)})

def payment(request):
    if not request.user.is_authenticated: 
        return redirect('../signin')
    pro = Profile.objects.filter(user = request.user).first()
    try:
        difference = (datetime.now() - pro.last_date_of_payment.replace(tzinfo=None)).days
        if difference < 30: 
            return redirect('../dashboard')
    except:
        pass
    
    if request.method == 'POST':
        transaction_id = CompletePayment()
        Payments.objects.create(
            user = request.user,
            amount = 500,
            transaction_id = transaction_id,
            date_of_payment = datetime.now(),
            slot = int(request.POST["slot"])
        )
        profile = Profile.objects.filter(user= request.user).first()
        profile.last_date_of_payment = datetime.now()
        profile.slot = int(request.POST["slot"])
        profile.save()
        
        return redirect('../dashboard')
    return render(request,"user/payment.html",)

def signout(request):
    logout(request)
    return redirect('../signin')