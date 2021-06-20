from django.urls import path
from . import views

urlpatterns = [
    path('TimeAndDist',views.TimeAndDist,name="TimeAndDist"),

]