from django.shortcuts import render
import mysql.connector as sql

em=''
pwd=''


# Create your views here.

def login_Activity(request):
    global em, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="vkk",passwd="vkk",database="django_Banao")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            s="@clinic.com"
            s1=em[-11:]
            print(s)
            print(s1)
            if s==s1:
                return render(request, 'doctor_Page.html')
            return render(request, 'patient_page.html')

    return render(request,'login.html')

