from django.urls import path
from . import views
urlpatterns = [
    path('studentRegister',views.studentRegister, name = 'studentRegister'),
    path('aptitude',views.aptitude,name = "aptitude"),
    path('cnotes',views.cnotes,name = "cnotes"),
    path('cppnotes',views.cppnotes,name = "cppnotes"),
    path('corejavanotes',views.corejavanotes,name = "corejavanotes"),
    path('advancejavanotes', views.advancejavanotes, name="advancejavanotes"),
    path('index', views.index, name="index"),
    path('pythonnotes', views.pythonnotes, name="pythonnotes"),
    path('arithmetic', views.arithmetic, name="arithmetic"),
    path('datainterpretation', views.datainterpretation, name="datainterpretation"),
    path('logical', views.logical, name="logical"),
    path('cquiz', views.cquiz, name="cquiz"),
    path('cppquiz', views.cppquiz, name="cppquiz"),
    path('corejavaquiz', views.corejavaquiz, name="corejavaquiz"),
    path('advancejavaquiz', views.advancejavaquiz, name="advancejavaquiz"),
    path('pythonquiz', views.pythonquiz, name="pythonquiz"),


]