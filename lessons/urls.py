from django.urls import path, include
from lessons.views import LessonListView, ProductLessonListView, ProductStatsView

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='product-lessons'),
    path('lessons/<int:product_id>/', ProductLessonListView.as_view(), name='product-lessons-by-product'),
    path('statistic/', ProductStatsView.as_view(), name='statistic'),
    path('auth/', include('rest_framework.urls')),
]
