from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
 # Creating Router Object
#router=DefaultRouter()

# Register StudentViewSet with Router
#router.register('studentapi', views.StudentModelViewSet, basename='student')
urlpatterns = [
    #path('stuinfo/', views.student_list)
    #path('stuinfo/',views.student_list,name="stuinfo"),
    path('',views.index,name="index"),
    path('studentapi/', views.StudentModelViewSet.as_view()),
    #path('', include(router.urls)),
    #path('studentapi/', views.StudentModelViewSet),
]