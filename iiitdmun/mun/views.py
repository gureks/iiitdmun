from django.shortcuts import render
from django.http import HttpResponseRedirect
import os
from django.views.static import serve

# Create your views here.
def index(request):
    return render(request,'index.html',{})
def register(request):
    return render(request,'forms/index.html',{})
def collegedelegation(request):
    return render(request,'forms/school.html',{})
def ip(request):
    return render(request,'forms/ip.html',{})
def individualdelegation(request):
    return render(request,'forms/individual.html',{})
#Forms follow here
def ipformsubmit(request):
    if request.method == "POST":
        fname=request.POST.get("first_name","")
        lname=request.POST.get("last_name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        city=request.POST.get("city","")
        link1=request.POST.get("affiliations","")
        link2=request.POST.get("comments","")
        link3=request.POST.get("experience","")
        file=open("ipforms","a")
        file.write(""+fname+" "+lname+","+email+","+phone+","+city+","+link1+","+link2+","+link3+"\n")
        file.close()
        return HttpResponseRedirect("../success/")
def indisubmit(request):
    if request.method =="POST":
        fname=request.POST.get("first_name","")
        lname=request.POST.get("last_name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        college=request.POST.get("college","")
        experience=request.POST.get("experience","")
        pref1=request.POST.get("pref1","")
        pref2=request.POST.get("pref2","")
        pref3=request.POST.get("pref3","")
        file=open("indiforms","a")
        file.write(""+fname+" "+lname+","+email+","+phone+","+college+","+experience+","+pref1+","+pref2+","+pref3+"\n")
        file.close()
        return HttpResponseRedirect("../success/")
def collsubmit(request):
    if request.method =="POST":
        fname=request.POST.get("first_name","")
        lname=request.POST.get("last_name","")
        phone=request.POST.get("phone","")
        link1=request.POST.get("affiliations1","")
        link2=request.POST.get("affiliations2","")
        link3=request.POST.get("affiliations3","")
        link4=request.POST.get("comments1","")
        link5=request.POST.get("affiliations4","")
        link6=request.POST.get("affiliations5","")
        link7=request.POST.get("comments2","")
        fname1=request.POST.get("first_name1","")
        fname2=request.POST.get("first_name2","")
        fname3=request.POST.get("first_name3","")
        fname4=request.POST.get("first_name4","")
        fname5=request.POST.get("first_name5","")
        fname6=request.POST.get("first_name6","")
        fname7=request.POST.get("first_name7","")
        lname1=request.POST.get("last_name1","")
        email=request.POST.get("email","")
        phone1=request.POST.get("phone1","")
        file=open("collforms","a")
        file.write(""+fname+","+lname+","+phone+","+link1+","+link2+","+link3+","+link4+","+link5+","+link6+","+link7+","+fname1+","+fname2+","+fname3+","+fname4+","+fname5+","+fname6+","+fname7+" "+lname1+","+email+","+phone1+"\n")
        file.close()
        return HttpResponseRedirect("../success/")
def consubmit(request):
    if request.method == "POST":
        email=request.POST.get("email","")
        passw=request.POST.get("pass","")
        mess=request.POST.get("mess","")
        file=open("conforms","a")
        file.write(""+email+","+passw+","+mess+"\n") 
        file.close()
        return HttpResponseRedirect("../../")
#successful submission        
def success(request):
    return render(request,'forms/formsubmitted.html',{})