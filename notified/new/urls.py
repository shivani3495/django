from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name="index"),
    #path('signal/', views.Notification1API.as_view()),
    #path('signal/', include(router.urls)),

    path('getting/', views.Notification1API.as_view()),
    path('creating/', views.Notification2API.as_view()),
    path('updating/', views.Notification3API.as_view()),
    path('deleting/<int:pk>/', views.Notification4API.as_view()),


]