from django.shortcuts import render,redirect
import psycopg2 as ps

def login(request):
    uname = "Not loged in"
    if request.method=="POST":
        uname ="'"+str(request.POST.get("uname"))+"'"
        pword ="'"+str(request.POST.get("upass"))+"'"
        con = ps.connect(database='Placement',user='postgres',password='test123',host='127.0.0.1',port='5432')
        cur = con.cursor()
        cur.execute('SELECT "FirstName","Email","Password" from public."Student_student" WHERE "Email"={} AND "Password"={};'.format(uname,pword))
        srows = cur.fetchall()
        print(srows)
        cur2 = con.cursor()
        cur2.execute('SELECT "FirstName","Email","Password","IsAdmin" from public."Teacher_teacher" WHERE "Email"={} AND "Password"={};'.format(uname, pword))
        trows = cur2.fetchall()
        if len(srows) == 1:
            name = ""
            for row in srows:
                name = row[0]
            request.session['uname'] = uname
            request.session['name'] = name
            return render(request, "index.html", {'username': name})
        elif len(trows) == 1:
            tname = ""
            admin = False
            for row in trows:
                tname = row[0]
                admin = row[3]

            if admin == True:
                cur3 = con.cursor()
                cur3.execute('SELECT compname from public.company;')
                crows = cur3.fetchall()
                cname = []
                for r in crows:
                    cname.append(r[0])
                request.session['name'] = tname
                request.session['uname'] = 'Admin'
                return render(request, "adminpanel.html", {'username': tname,'cname':cname})
            else:
                request.session['uname'] = uname
                request.session['name'] = tname
                return render(request, "teacherpanel.html", {'username': tname})
        else:
            return render(request,"login.html",{'res':'Invalid user'})

    return render(request, "login.html", {})


def logout(request):
    try:
        del request.session['uname']
        del request.session['name']
    except:
        pass
    return redirect('/')