from rest_framework.views import APIView
from rest_framework.response import Response

from lessons.models import LessonView, ProductAccess, Product
from lessons.serializers import ProductLessonsSerializer, ProductStatisticsSerializer

from lessons.serializers import ProductLessonsByProductSerializer


class ProductLessonsView(APIView):
    def get(self, request):
        user = request.user
        products = ProductAccess.objects.filter(user=user).values_list('product', flat=True)
        lessons = LessonView.objects.filter(user=user, lesson__products__in=products)
        serialized_lessons = ProductLessonsSerializer(lessons, many=True)
        return Response(serialized_lessons.data)


class ProductStatisticsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialized_products = ProductStatisticsSerializer(products, many=True)
        return Response(serialized_products.data)


class ProductLessonsByProductView(APIView):
    def get(self, request, product_id):
        user = request.user
        try:
            product = ProductAccess.objects.get(user=user, product_id=product_id)
        except ProductAccess.DoesNotExist:
            return Response("Access to the product is not granted.")
        lessons = LessonView.objects.filter(user=user, lesson__products=product.product)
        serialized_lessons = ProductLessonsByProductSerializer(lessons, many=True)
        return Response(serialized_lessons.data)