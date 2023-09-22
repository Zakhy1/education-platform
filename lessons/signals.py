from django.db.models.signals import post_save
from django.dispatch import receiver

from lessons.models import ProductAccess, LessonView


@receiver(post_save, sender=ProductAccess)
def create_user_profile(sender, instance, created, **kwargs):
    """
     # Мне кажется это мега костыль, но другого способа выводить все уроки,
     вне зависимости есть у них связанный объект LessionView
    """

    if created:  # Если создан объект доступа к продукту, то создается объект просмотра всех уроков в продукте
        for lesson in instance.product.lesson_set.all():
            LessonView.objects.create(user=instance.user, lesson=lesson)
