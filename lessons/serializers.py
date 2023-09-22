from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers
from .models import LessonView, Product, ProductAccess, Lesson


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class ProductStatsSerializer(serializers.ModelSerializer):
    total_lessons_viewed = serializers.SerializerMethodField()
    total_view_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    acquisition_percent = serializers.SerializerMethodField()

    def get_total_lessons_viewed(self, obj):
        lesson_views = LessonView.objects.filter(viewed=True, lesson__products=obj)
        return lesson_views.count()

    def get_total_view_time(self, obj):
        lesson_views = LessonView.objects.filter(lesson__products=obj)
        return lesson_views.aggregate(Sum('view_time')).get('view_time__sum', 0)

    def get_total_students(self, obj):
        return ProductAccess.objects.filter(product=obj).count()

    def get_acquisition_percent(self, obj):
        total_users = User.objects.count()
        return ProductAccess.objects.filter(product=obj).count() / total_users * 100

    class Meta:
        model = Product
        fields = ('id', 'title', 'total_lessons_viewed', 'total_view_time', 'total_students', 'acquisition_percent')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'video_link', 'duration')


class LessonViewSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return 'Viewed' if obj.viewed else 'Not viewed'

    class Meta:
        model = LessonView
        fields = ('lesson', 'status', 'view_time', 'last_view_date')


class ProductLessonViewSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title')
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return 'Viewed' if obj.viewed else 'Not viewed'

    class Meta:
        model = LessonView
        fields = ('lesson_title', 'status', 'view_time', 'last_view_date')
