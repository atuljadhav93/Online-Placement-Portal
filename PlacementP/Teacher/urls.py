from django.urls import path
from . import views

urlpatterns = [
    path('adminpanel', views.adminpanel, name="adminpanel"),
    #path('teacherpanel',views.teacherpanel,name="teacherpanel"),
    path('teacherRegister',views.teacherRegister, name = 'teacherRegister'),
    path('studentDetails',views.studentDetails,name="studentDetails"),
    path('studRegistreDetails',views.studRegistreDetails,name="studRegistreDetails"),
    path('companyDetails',views.companyDetails,name="companyDetails"),
    path('addNotification',views.addNotification,name="addNotification"),


]
