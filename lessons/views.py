from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from lessons.models import LessonView, Product
from lessons.serializers import LessonViewSerializer, ProductLessonViewSerializer, \
    ProductStatsSerializer


class LessonListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        lesson_views = LessonView.objects.filter(user=user)
        serializer = LessonViewSerializer(lesson_views, many=True)
        return Response(serializer.data)


class ProductLessonListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id):
        user = request.user
        product = get_object_or_404(Product, id=product_id)
        lesson_views = LessonView.objects.filter(user=user, lesson__products=product)
        serializer = ProductLessonViewSerializer(lesson_views, many=True)
        return Response(serializer.data)


class ProductStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductStatsSerializer(products, many=True)
        return Response(serializer.data)
