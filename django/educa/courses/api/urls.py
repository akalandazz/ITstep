from django.urls import path
from . import views
from django.urls import path, include 
from rest_framework import routers

app_name = 'courses'

router = routers.DefaultRouter() 
router.register('courses', views.CourseViewSet)
router.register('subjects', views.SubjectViewSet)



urlpatterns = [
	path('', include(router.urls))
	]