from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import json
from .forms import registerForm
from .models import Admin, Contact, register, Feedback
from django.contrib import messages



def home(request):
    return render(request,"index.html")
def adminhome(request):
    return render(request,"adminhome.html")

def Logout(request):
    return render(request,"login.html")

def registration(request):
    form=registerForm()
    if request.method == "POST":
        form1=registerForm(request.POST)
        if form1.is_valid():
            form1.save()
            msg = "Successfully Registered"
            return render(request,"register.html",{"msg":msg,"form":form})
        else:
            msg = "Failed Registration"
            return render(request, "register.html", {"msg": msg,"form":form})
    return render(request,"register.html",{"form":form})

def checkadminlogin(request):
    registerid=request.POST["rid"]
    registerpwd=request.POST["rpwd"]
    flag=register.objects.filter(Q(username=registerid)&Q(password=registerpwd))
    print(flag)


    if flag:
        return render(request,"adminhome.html")
    else:
        return HttpResponse("login failed")

def contactsave(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message=request.POST['message']
        new_id = Contact(name=name,email=email,message=message)
        new_id.save()
        return redirect('contactus')

def contactus(request):
    return render(request,"contact.html")

def rasi(request):
    if request.method == "POST":
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        date = int(request.POST.get('date'))
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))
        url = "https://json.freeastrologyapi.com/horoscope-chart-svg-code"
        payload = json.dumps({
            "year": year,
            "month": month,
            "date": date,
            "hours": hours,
            "minutes": minutes,
            "seconds": 0,
            "latitude": 17.38333,
            "longitude": 78.4666,
            "timezone": 5.5,
            "config": {
                "observation_point": "topocentric",
                "ayanamsha": "lahiri"
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'sVhJNyXEho1paRvj6HgqK61jX3Xfef1xaGkD982m'
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            # Parse the JSON response
            response_json = response.json()
            # Extract SVG data from the response
            svg_data = response_json.get("output", "")

            if svg_data:
                # Pass SVG data to the template
                return render(request, "userinput.html", {"svg_data": svg_data})

        return render(request, "rasichart.html", {"svg_data": None})


def input(request):
    return render(request,"userinput.html")

def forget(request):
    return render(request,"forget.html")
def feedback(request):
    count = Feedback.objects.count()
    feedback_data = Feedback.objects.all()
    return render(request, "feedback.html", {"count": count, "data": feedback_data})

def submit_feedback(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')

        feedback = Feedback(
            customer_name=customer_name,
            email=email,
            feedback=feedback_text,
        )
        feedback.save()
        messages.info(request, "Feedback submitted successfully")
        return redirect('feedback')


def userupdatepwd(request):
    uname = request.POST["uname"]
    opwd = request.POST["opwd"] 
    npwd = request.POST["npwd"]
    flag = register.objects.filter(Q(username=uname) & Q(password=opwd))
    if flag:
        register.objects.filter(username=uname).update(password=npwd)
        msg = "Password Updated Successfully"
    else:
        msg = "Old Password is Incorrect"
    return render(request, "login.html", {"uname": uname, "message": msg})


def nakshatra(request):
    url = "https://json.freeastrologyapi.com/nakshatra-durations"

    payload = json.dumps({
        "year": 2022,
        "month": 8,
        "date": 11,
        "hours": 6,
        "minutes": 0,
        "seconds": 0,
        "latitude": 17.38333,
        "longitude": 78.4666,
        "timezone": 5.5,
        "config": {
            "observation_point": "topocentric",
            "ayanamsha": "lahiri"
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'WXzOw5ce134Kr9rN68iWa1vBIYDWPitI5ifoSnFB'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def input1(request):
    return render(request,"nakshatra.html")