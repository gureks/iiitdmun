from django.shortcuts import render
from django.http import HttpResponseRedirect
from hashlib import md5
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
    return render(request,'forms/index.html',{})
def individualdelegation(request):
    return render(request,'forms/individual.html',{})
def ipformsubmit(request):
    if request.method == "POST":
        fname=request.POST.get("first_name","")
        lname=request.POST.get("last_name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        city=request.POST.get("city","")
        link1=request.POST.get("affiliations","")
        link2=request.POST.get("comments","")
        link3=request.POST.get("affiliations1","")
        file=open("ipforms","a")
        file.write(" Name: "+fname+" "+lname+" \n Email: "+email+" \n Phone: "+phone+" \n Applying for: "+city+" \n Links to your work : "+link1+" \n Link to your samplework : "+link2+" \n Previous experiences: "+link3+"\n"+"\n"+"\n")
        file.close()
        return HttpResponseRedirect("../success/")
def indisubmit(request):
    if request.method =="POST":
        fname=request.POST.get("first_name","")
        lname=request.POST.get("last_name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        city=request.POST.get("city","")
        link1=request.POST.get("affiliations","")
        link2=request.POST.get("comments","")
        link3=request.POST.get("affiliations1","")
        file=open("indiforms","a")
        file.write(" Name: "+fname+" "+lname+" \n Email: "+email+" \n Phone: "+phone+" \n Committees allotment preferences: "+city+" \n Links to your work : "+link1+" \n Link to your samplework : "+link2+" \n Previous experiences: "+link3+"\n"+"\n"+"\n")
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
        link6=request.POST.get("comments2","")
        fname1=request.POST.get("first_name1","")
        fname2=request.POST.get("first_name2","")
        fname3=request.POST.get("first_name3","")
        fname4=request.POST.get("first_name4","")
        fname5=request.POST.get("first_name5","")
        fname6=request.POST.get("first_name6","")
        lname1=request.POST.get("last_name1","")
        email=request.POST.get("email","")
        phone1=request.POST.get("phone1","")
        file=open("collforms","a")
        file.write(" Name of Institution : "+fname+" \n Address: "+lname+" \n Phone: "+phone+" \n Allotment Preferences for GA:ESS: "+link1+" \n Allotment Preferences for SPECPOL: "+link2+" \n Allotment Preferences for NSC: "+link3+" \n Allotment Preferences for UNSC: "+link4+" \n Allotment Preferences for WIPO: "+link5+" \n Details of delegates: "+link6+" \n GA ESS: "+fname1+" \n SPECPOL: "+fname2+" \n NSC: "+fname3+" \n UNSC: "+fname4+" \n WIPO: "+fname5+" \n Name of Head: "+fname6+" "+lname1+" \n Email: "+email+" \n Phone: "+phone1+"\n"+"\n"+"\n")
        file.close()
        return HttpResponseRedirect("../success/")
def consubmit(request):
    if request.method == "POST":
        email=request.POST.get("email","")
        passw=request.POST.get("pass","")
        mess=request.POST.get("mess","")
        file=open("conforms","a")
        file.write(" Email: "+email+" \n Password: "+passw+" \n Message: "+mess+"\n \n \n") 
        file.close()
        return HttpResponseRedirect("../../")
        
def success(request):
    return render(request,'forms/formsubmitted.html',{})
        
        
        
        
        
        
        
