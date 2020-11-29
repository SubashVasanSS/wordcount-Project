
from django.urls import path
from . import views


urlpatterns = [
    path('',views.homePage,name="home"),
   path('count/',views.countMe,name="count"),
   path('about/',views.about,name="about")
]
