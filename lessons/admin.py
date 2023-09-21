from django.contrib import admin

from lessons.models import Lesson, LessonView


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "duration"]
    search_fields = ["title"]


@admin.register(LessonView)
class LessonViewAdmin(admin.ModelAdmin):
    list_display = ["lesson", "view_time", "viewed"]
    list_filter = ["lesson", "viewed"]
    search_fields = ["user"]
