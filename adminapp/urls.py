from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.Logout,name="adminlogout"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("registration", views.registration, name="registration"),
    path('contactus',views.contactus,name='Home-contact'),
    path('rasi/', views.rasi, name='rasi'),
    path('input',views.input,name="input"),
    path('userupdatepwd',views.userupdatepwd,name="userupdatepwd"),
    path('feedback',views.feedback,name="feedback"),
    path('submit_feedback',views.submit_feedback,name="submit_feedback"),
    path('nakshatra',views.nakshatra,name="nakshatra"),
    path('input1/', views.input1, name='input1'),
]
