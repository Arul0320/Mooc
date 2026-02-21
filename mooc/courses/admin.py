from django.contrib import admin

# Register your models here.
admin.site.site_header = "MOOC Admin"
admin.site.index_title = "Welcome to MOOC Admin Portal"
from .models import Course, Lesson, Enrollment, LessonProgress
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at')
    search_fields = ('title', 'course__title')
    ordering = ('-created_at',)
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__username', 'course__title')
    ordering = ('-enrolled_at',)        
    
@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'visited', 'visited_at')
    search_fields = ('user__username', 'lesson__title')
    ordering = ('-visited_at',)    