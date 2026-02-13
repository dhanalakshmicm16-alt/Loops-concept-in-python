from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_add'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_add'),
    path('marks/add/', views.marks_create, name='marks_add'),
]
