from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db import connection
# Create your views here.
def registration(request):
    if request.method=="POST":
        first_name =  request.POST['first_name']
        email = request.POST['email']
        CollegeName = request.POST['CollegeName']
        Semester = request.POST['Semester']
        PhoneNumber = request.POST['PhoneNumber']
        EventName = request.POST['EventName']
        with connection.cursor() as cursor:
            cursor.execute("insert into main_urd values('{0}','{1}','{2}',{3},{4},'{5}')".format(first_name,email,CollegeName,Semester,PhoneNumber,EventName))
            connection.commit()
            
        return redirect('base')
    else:
        events_list=[]
        with connection.cursor() as cursor:
            cursor.execute('select name from main_events')
            events_list=cursor.fetchall()
            events_list=[item[0] for item in events_list]
        return render(request,'registration.html',{'events':events_list})