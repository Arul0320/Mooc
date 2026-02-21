from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/<int:pk>/enroll/", views.enroll_course, name="enroll_course"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("lessons/<int:pk>/", views.lesson_detail, name="lesson_detail"),
]
