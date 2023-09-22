from django.urls import path, include
from lessons.views import ProductLessonsView, ProductStatisticsView, ProductLessonsByProductView

urlpatterns = [
    path('lessons/', ProductLessonsView.as_view(), name='product-lessons'),
    path('lessons/<int:product_id>/', ProductLessonsByProductView.as_view(), name='product-lessons-by-product'),
    path('statistic/', ProductStatisticsView.as_view(), name='statistic'),
    path('auth/', include('rest_framework.urls')),
]
