from django.shortcuts import render, redirect
import mysql.connector as sql
from django.http import HttpResponse
from .forms import * 

fn=''
ln=''
pp=''
un=''
em=''
pwd=''
cpwd=''
ad=''
sta=''
cit=''
pin=''


# Create your views here.

def register_Activity(request):
    global fn, ln, pp, un, em, pwd, cpwd, ad, sta, cit, pin
    if request.method=="POST":
        m=sql.connect(host="localhost",user="vkk",passwd="vkk",database="django_Banao")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="f_name":
                fn=value
            if key=="l_name":
                ln=value
            if key=="p_picture":
                pp=value
            if key=="u_name":
                un=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="confirm_password":
                cpwd=value
            if key=="address":
                ad=value
            if key=="state":
                sta=value
            if key=="city":
                cit=value
            if key=="pincode":
                pin=value

        if pwd!=cpwd:
            return render(request, 'errorNotM.html')
            
        c="insert into users values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,pp,un,em,pwd,ad,sta,cit,pin)
        cursor.execute(c)
        m.commit()

    return render(request,'register.html')



def addimg(request):
    return render(request,'add_img.html')  

def homep(request):
    return render(request, 'index.html')

  