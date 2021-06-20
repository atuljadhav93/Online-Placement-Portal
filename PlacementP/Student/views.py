from django.shortcuts import render,redirect
from .models import Student


# Create your views here.
def studentRegister(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        mname = request.POST.get("middlename")
        lname = request.POST.get("lastname")
        mobile = request.POST.get("mobileno")
        amobile = request.POST.get("alternetmobileno")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        lang1 = request.POST.get("CBEnglish")
        lang2 = request.POST.get("CBHindi")
        lang3 = request.POST.get("CBMarathi")
        address = request.POST.get("address")
        DateOfBirth = request.POST.get("birthdate")
        SCName10 = request.POST.get("schoolname")
        Percentage10 = request.POST.get("tenthpercent")
        BoardName10 = request.POST.get("selecttenthboard")
        OtherBoardName10 = request.POST.get("tenthboard")
        PassingYear10 = request.POST.get("passyear")
        CollegeName12 = request.POST.get("twelvecollege")
        Percentage12 = request.POST.get("twelvepercent")
        PassingYear12 = request.POST.get("twelvepassyear")
        BoardName12 = request.POST.get("twelveexamboard")
        OtherBoardName12 = request.POST.get("twelveboard")
        DiplomaInstitue = request.POST.get("diplomainstitute")
        DiplomaPercentage = request.POST.get("diplomapercentage")
        PassingYearDiploma = request.POST.get("diplomapassyear")
        UGDegreeName = request.POST.get("selectugdegree")
        OtherUGDegree = request.POST.get("ugdegree")
        UGFYPercent = request.POST.get("fypercent")
        UGSYPercent = request.POST.get("sypercent")
        UGTYPercent = request.POST.get("typercent")
        PassingYearUG = request.POST.get("ugpassyear")
        CollegeNameUG = request.POST.get("ugcollege")
        UGUniversity = request.POST.get("uguniversity")
        PGDegreeName = request.POST.get("pgdegree")
        PGFYPercent = request.POST.get("pgfypercent")
        PGSYPercent = request.POST.get("pgsypercent")
        PassingYearPG = request.POST.get("pgpassyear")
        CollegeNamePG = request.POST.get("pgcollegename")
        PGUniversity = request.POST.get("pguniversity")
        IsGap = request.POST.get("isgap")
        YearGap = request.POST.get("yeargap")
        UGProjectName = request.POST.get("ugproject")
        UGProjectTech = request.POST.get("ugprojecttech")
        UGProjectDesc = request.POST.get("ugprojectdesc")
        PGProjectName = request.POST.get("pgproject")
        PGProjectTech = request.POST.get("pgprojecttech")
        PGProjectDesc = request.POST.get("pgprojectdesc")

        if Student.objects.filter(FirstName=fname).exists() and Student.objects.filter(MiddleName=mname).exists() and Student.objects.filter(LastName=lname).exists() and Student.objects.filter(Email=email).exists() and Student.objects.filter(Mobile=mobile).exists() and Student.objects.filter(AMobile=amobile).exists():
            return render(request,"login.html",{'res':'Student Already Exists...'})
        else:
            stud = Student()
            stud.FirstName = fname
            stud.MiddleName = mname
            stud.LastName = lname
            stud.Mobile = mobile
            stud.AMobile = amobile
            stud.Email = email
            stud.Password = password
            stud.gender= gender
            stud.DateOfBirth = DateOfBirth
            stud.Address = address
            stud.Lang1 = lang1
            stud.Lang2 = lang2
            stud.Lang3 =lang3
            stud.SchoolName10th = SCName10
            stud.BoardName10th = BoardName10
            stud.Percentage10th = Percentage10
            stud.PassingYear10th = PassingYear10
            stud.CollegeName12th = CollegeName12
            stud.BoardName12th = BoardName12
            stud.Percentage12th = Percentage12
            stud.PassingYear12th = PassingYear12
            stud.DiplomaInstituteName= DiplomaInstitue
            stud.PercentageDiploma = DiplomaPercentage
            stud.PassingYearDiploma = PassingYearDiploma
            stud.UGDegree = UGDegreeName
            stud.UGCollegeName= CollegeNameUG
            stud.UGUniversity = UGUniversity
            stud.UGFYPercentage = UGFYPercent
            stud.UGSYPercentage = UGSYPercent
            stud.UGTYPercentage = UGTYPercent
            stud.UGPassingYear = PassingYearUG
            stud.PGDegree = PGDegreeName
            stud.PGCollegeName= CollegeNamePG
            stud.PGUniversity = PGUniversity
            stud.PGFYPercentage = PGFYPercent
            stud.PGSYPercentage = PGSYPercent
            stud.PGTYPercentage = 0
            stud.PGPassingYear = PassingYearPG
            stud.GAP = YearGap
            stud.ProjectName1 = UGProjectName
            stud.ProjectTechnology1 = UGProjectTech
            stud.ProjectDesc1 = UGProjectDesc
            stud.ProjectName2 = PGProjectName
            stud.ProjectTechnology2 = PGProjectTech
            stud.ProjectDesc2 = PGProjectDesc
            stud.save()
            return redirect("/",{'res':'Registration Successful...'})

    else:
        return render(request,"signupstudent.html",{'res':'Something Went Wrong...'})


def index(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"index.html",{'username':uname})
    else:
        return render(request,"login.html",{})

def aptitude(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"arithmeticnotes.html",{'username':uname})
    else:
        return render(request,"login.html",{})


def cnotes(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"cnotes.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def cppnotes(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"c++notes.html",{'username':uname})
    else:
        return render(request, "login.html", {})


def corejavanotes(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"corejavanotes.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def advancejavanotes(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"advancejavanotes.html",{'username':uname})
    else:
        return render(request, "login.html", {})


def pythonnotes(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"pythonnotes.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def arithmetic(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"arithmetic.html",{'username':uname})
    else:
        return render(request, "login.html", {})


def datainterpretation(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"datainterpretation.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def logical(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"logical.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def cquiz(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"c.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def cppquiz(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"c++.html",{'username':uname})
    else:
        return render(request, "login.html", {})


def corejavaquiz(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"corejava.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def advancejavaquiz(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"advancejava.html",{'username':uname})
    else:
        return render(request, "login.html", {})

def pythonquiz(request):
    if request.session.has_key('uname'):
        uname = request.session['name']
        return render(request,"python.html",{'username':uname})
    else:
        return render(request, "login.html", {})