from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменения")

    deleted = models.BooleanField(default=False, verbose_name="Удален")

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class News(BaseModel):
    """Определяем модель для Новостей"""
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    preambule = models.CharField(max_length=256, verbose_name="Вступление")
    text = models.TextField(blank=True, null=True,
                            verbose_name="Teкст новости")
    main_picture = models.ImageField(
        blank=True, verbose_name="Главное изображение", upload_to='news/%Y/%m/%d')

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta():
        verbose_name_plural = "Новости"
        verbose_name = "Новость"


class NewsImages(models.Model):
    news = models.ForeignKey(News, default=None, related_name='images',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = "Изображение для новости"
        verbose_name_plural = "Изображения для новости"
