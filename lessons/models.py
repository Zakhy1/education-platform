from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars


class Product(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} has access to {self.product.title}"


class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()  # Длительность в секундах

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.IntegerField(default=0)  # Время просмотра в секундах
    viewed = models.BooleanField(default=False)
    last_view_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Проверяем, просмотрено ли 80% урока
        if self.view_time >= self.lesson.duration * 0.8:
            self.viewed = True
        else:
            self.viewed = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}: {self.viewed}"
