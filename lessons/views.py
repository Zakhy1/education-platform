from rest_framework.views import APIView
from rest_framework.response import Response

from lessons.models import LessonView
from lessons.serializer import ProductLessonsSerializer
from products.models import ProductAccess


class ProductLessonsView(APIView):
    def get(self, request):
        user = request.user
        products = ProductAccess.objects.filter(user=user).values_list('product', flat=True)
        lessons = LessonView.objects.filter(user=user, lesson__products__in=products)
        serialized_lessons = ProductLessonsSerializer(lessons, many=True)
        return Response(serialized_lessons.data)
