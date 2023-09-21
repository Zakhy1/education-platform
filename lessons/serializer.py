from rest_framework import serializers

from lessons.models import Lesson
from products.models import Product


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'video_link', 'duration')


class ProductLessonsSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'lessons')
