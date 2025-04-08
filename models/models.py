from django.db import models
from django.conf import settings


class Model(models.Model):
    file = models.FileField(upload_to='models_upload/models', verbose_name='Файл')
    image = models.ImageField(upload_to='models_upload/images', verbose_name='Изображение', blank=True, null=True)
    name = models.TextField(max_length=30, verbose_name='Название', blank=True, null=True)
    description = models.TextField(max_length=500, verbose_name='Описание', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    cnt_downloads = models.IntegerField(default=0, verbose_name='Количество загрузок')
    cnt_likes = models.IntegerField(default=0, verbose_name='Количество лайков')

    def __str__(self):
        return f"Модель {self.name} от {self.author}"

    def get_absolute_url(self):
        pass


class Comment(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='comments', verbose_name="Комментарий")
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name = "Автор"
    )

    def __str__(self):
        return f"Комментарий {self.author} к {self.model}"

    def get_absolute_url(self):
        return Model.objects.get(id=self.model.id).get_absolute_url()

class Like(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='likes', verbose_name="Лайк")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name = "Автор"
    )

    def __str__(self):
        return f"Лайк {self.author} к {self.model}"

    def get_absolute_url(self):
        return Model.objects.get(id=self.model.id).get_absolute_url()
