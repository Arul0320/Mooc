from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Enrollment, LessonProgress
from .forms import SignupForm


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "registration/signup.html", {"form": form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()

    progress = LessonProgress.objects.filter(user=request.user).values_list("lesson_id", flat=True) if request.user.is_authenticated else []

    return render(request, "courses/course_detail.html", {
        "course": course,
        "lessons": lessons,
        "is_enrolled": is_enrolled,
        "progress": progress
    })


@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect("course_detail", pk=pk)


@login_required
def my_courses(request):
    courses = Course.objects.filter(enrollment__user=request.user)
    return render(request, "courses/my_courses.html", {"courses": courses})


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)

    return render(request, "courses/lesson_detail.html", {"lesson": lesson})
