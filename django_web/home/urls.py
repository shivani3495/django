from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('contact',views.myfunctioncontact,name="contact"),
    path('login',views.myfunctionlogin,name="login"),
    path('register',views.myfunctionregister,name="register"),
    path('profile',views.myfunctionprofile,name="profile"),
    path('Logout',views.logout,name="logout"),
    path('edit',views.edit,name="edit"),
    path('editnew',views.editnew,name="editnew"),
    path('delete',views.delete,name="delete"),
    path('home',views.home,name="home")
   
]