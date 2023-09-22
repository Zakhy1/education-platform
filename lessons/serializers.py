from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

from lessons.models import Lesson, Product, ProductAccess, LessonView


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'video_link', 'duration')


class ProductLessonsSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'lessons')


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ('lesson', 'view_time', 'viewed')


class ProductLessonsByProductSerializer(serializers.ModelSerializer):
    lessons = LessonViewSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'lessons')


class ProductStatisticsSerializer(serializers.ModelSerializer):
    total_lessons_viewed = serializers.SerializerMethodField()
    total_view_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    product_percentage = serializers.SerializerMethodField()

    def get_total_lessons_viewed(self, obj):
        return LessonView.objects.filter(lesson__products=obj).count()

    def get_total_view_time(self, obj):
        return LessonView.objects.filter(lesson__products=obj).aggregate(total_time=models.Sum('view_time')).get(
            'total_time')

    def get_total_students(self, obj):
        return ProductAccess.objects.filter(product=obj).count()

    def get_product_percentage(self, obj):
        total_users = User.objects.count()
        product_access = ProductAccess.objects.filter(product=obj).count()
        return (product_access / total_users) * 100

    class Meta:
        model = Product
        fields = ('id', 'name', 'total_lessons_viewed',
                  'total_view_time', 'total_students', 'product_percentage')
