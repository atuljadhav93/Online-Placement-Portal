from django.shortcuts import render,redirect
from .models import Teacher
import psycopg2 as ps

#Create your views here.
def adminpanel(request):
    if request.session.has_key('uname'):
        uname = request.session['uname']
        name = request.session['name']
        if uname == 'Admin':
            con = ps.connect(database='Placement', user='postgres', password='test123', host='127.0.0.1', port='5432')
            cur3 = con.cursor()
            cur3.execute('SELECT compname from public.company;')
            crows = cur3.fetchall()
            cname = []
            for r in crows:
                cname.append(r[0])
            return render(request, "adminpanel.html", {'username': name,'cname':cname})
    else:
        return render(request, "login.html", {})

#def teacherpanel(request):
#    if request.session.has_key('uname'):
#        uname = request.session['uname']
#        name = request.session['name']
#        if uname != 'Admin':
#            return render(request,"adminpanel.html",{'username':name})
#    else:
#        return render(request,"login.html",{})

def studentDetails(request):
    if request.session.has_key('uname'):
        uname = request.session['uname']
        name = request.session['name']
        return render(request,"studentdetails.html",{'username':name})
    else:
        return render(request, "login.html", {})


def studRegistreDetails(request):
    if request.session.has_key('uname'):
        uname = request.session['uname']
        name = request.session['name']
        if uname == 'Admin':
            return render(request, "studentregistrationdetails.html", {'username': name})
    else:
        return render(request, "login.html", {})

def companyDetails(request):
    if request.session.has_key('uname'):
        uname = request.session['uname']
        name = request.session['name']
        if request.method=="POST":
            con = ps.connect(database='Placement', user='postgres', password='test123', host='127.0.0.1', port='5432')
            cur = con.cursor()
            cur1 = con.cursor()
            cur1.execute("Select compid from public.company;")
            cnt = 0
            rcid = cur1.fetchall()
            for i in rcid:
                cnt = cnt+1

            cnt = cnt+1
            comanyName = request.POST.get('CompName')
            CompAddress = request.POST.get('CompAddress')
            CompPhone = request.POST.get('CompPhone')
            CompEmail = request.POST.get('CompEmail')
            CompDetails = request.POST.get('CompDetails')

            cur.execute("INSERT INTO public.company(compid,compname,compemail,compphone,compaddress,compdetails) VALUES({},'{}','{}',{},'{}','{}')".format(cnt,comanyName,CompEmail,CompPhone,CompAddress,CompDetails))
            con.commit()
            info = "Company Details Added succeessfully..."
            return render(request, "companydetails.html", {'username': name,'info':info})
        else:
            return render(request, "companydetails.html", {'username': name})
    else:
        return render(request, "login.html", {})


def addNotification(request):
    if request.session.has_key('uname'):
        uname = request.session['uname']
        tname = request.session['name']
        if request.method=="POST":
            con = ps.connect(database='Placement', user='postgres', password='test123', host='127.0.0.1', port='5432')
            cur = con.cursor()
            cur1 = con.cursor()
            comanyName = request.POST.get('companyname')
            sDate = request.POST.get('startDate')
            eDate = request.POST.get('endDate')
            message = request.POST.get('msg')
            #sd = sDate.split('-')
            #ed = eDate.split('-')
            #startDate = ''+str(sd[2])+'-'+str(sd[1])+'-'+str(sd[0])
            #endDate = ''+str(ed[2])+'-'+str(ed[1])+'-'+str(ed[0])

            cur1.execute("SELECT compid from public.company where compname='{}';".format(comanyName))
            crow = cur1.fetchall()
            cid = 0
            for i in crow:
                cid = i[0]
            cur.execute("INSERT INTO public.compnotification(compid,startdate,enddate,message) VALUES({},'{}','{}','{}')".format(cid,sDate,eDate,message))
            con.commit()
            info = "Notification posted succeessfully..."
            cur3 = con.cursor()
            cur3.execute('SELECT compname from public.company;')
            crows = cur3.fetchall()
            cname = []
            for r in crows:
                cname.append(r[0])
            return render(request, "adminpanel.html", {'username': tname, 'cname': cname, 'info':info})
        else:
            return render(request, "adminpanel.html", {'username': tname})
    else:
        return render(request, "login.html", {})


def teacherRegister(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        mname = request.POST.get('middlename')
        lname = request.POST.get('lastname')
        mob = request.POST.get('mobileno')
        amob = request.POST.get('alternetmobileno')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        DOB = request.POST.get('birthdate')
        course = request.POST.get('selectcourse')


        if Teacher.objects.filter(FirstName=fname).exists() and Teacher.objects.filter(MiddleName=mname).exists() and Teacher.objects.filter(LastName=lname).exists() and Teacher.objects.filter(Email=email).exists() and Teacher.objects.filter(Mobile=mob).exists() and Teacher.objects.filter(AlternateMobile=amob).exists():
            return render(request,"login.html",{'res':'Teacher Already Exists...'})
        else:
            t = Teacher()
            t.FirstName = fname
            t.MiddleName = mname
            t.LastName = lname
            t.Mobile = mob
            t.AlternateMobile = amob
            t.Email = email
            t.Password = password
            t.Gender = gender
            t.DateOfBirth = DOB
            t.Course = course
            t.IsAdmin = True
            t.save()
            return redirect("/", {'res': 'Registration Successful...'})
    else:
        return render(request,"signupteacher.html")
