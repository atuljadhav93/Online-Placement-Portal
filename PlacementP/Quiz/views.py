from django.shortcuts import render,redirect
import psycopg2 as ps
import time
# Create your views here.

def quiz(topic):
    con = ps.connect(database='Placement', user='postgres', password='test123', host='127.0.0.1', port='5432')
    cur = con.cursor()
    SID = 1#cur.execute("select sid from public.Subject where subject='"+str(topic)+"';")
    cur.execute("select question,optna,optnb,optnc,optnd FROM questions OFFSET floor(random() * (SELECT COUNT(*) FROM questions Where sid = {})) LIMIT 2;".format(SID))
    rows = cur.fetchall()
    qno = 0
    que=[]
    for row in rows:
        qno = qno+1
        q = ""+str(qno)
        #print(row)
        d = {"Qno":qno,"Que":row[0],"A":row[1],"B":row[2],"C":row[3],"D":row[4]}
        que.append(d)

    if qno !=2:
        quiz(topic)
    else:
        return que



def TimeAndDist(request):
    que = quiz("Time and Distance")
    print(que)
    return render(request,"quize.html",{'que':que})