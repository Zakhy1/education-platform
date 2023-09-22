from django.contrib import admin

from lessons.models import Lesson, LessonView, Product, ProductAccess


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration']
    search_fields = ['title']


@admin.register(LessonView)
class LessonViewAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'view_time', 'viewed', 'user']
    list_filter = ['lesson', 'viewed']
    search_fields = ['user']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ['user']
