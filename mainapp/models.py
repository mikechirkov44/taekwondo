from django.db import models
from django.core.validators import RegexValidator


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
        blank=True, verbose_name="Главное изображение", upload_to='img/')

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta():
        verbose_name_plural = "Новости"
        verbose_name = "Новость"


class NewsImages(models.Model):
    news = models.ForeignKey(News, default=None, related_name='images',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/', blank=True)

    class Meta:
        verbose_name = "Изображение для новости"
        verbose_name_plural = "Изображения для новости"


class Contact(models.Model):
    """Определяем модель для формы обратной связи"""

    CHOICES_HALLS = (
        ('1', 'С/К Спартак'),
        ('2', 'Ф/К Апельсин'),
        ('3', 'Лицей №41'),
        ('4', 'Гимназия №25'),
        ('5', 'Школа №21'),
        ('6', 'Школа №31'),
        ('7', 'Дворец Культуры'),
        ('8', 'Школа №37'),
        ('9', 'Отель "Третьяков"'),
        ('10', 'С/К "Синия птица"'),
        ('11', 'Зал единоборств'),

    )

    CHOICES_COACHES = (
        ('1', 'Маклаков В.П.'),
        ('2', 'Шустова М.А.'),
        ('3', 'Соколов П.И.'),
        ('4', 'Кошкаров Б.Н.'),
        ('5', 'Цыварев И.В.'),
        ('6', 'Сер А.Р.'),
        ('7', 'Усачева О.А.'),
    )

    parents_name = models.CharField(
        max_length=200, verbose_name="ФИО родителя")
    child_name = models.CharField(max_length=50, verbose_name="ФИО ребенка")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст ребенка")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name="Номер телефона")
    hall = models.CharField(max_length=200, unique=False,
                            verbose_name="Зал для тренировок", choices=CHOICES_HALLS)
    coach_name = models.CharField(
        unique=False, max_length=200, verbose_name="ФИО тренера", choices=CHOICES_COACHES)
    request_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата заявки")
    is_contacted = models.BooleanField(default=False, verbose_name="Связались")

    def __str__(self) -> str:
        return f'{self.parents_name} - {self.phone_number}'

    class Meta():
        verbose_name_plural = " Контакты"
        verbose_name = "Контакт"
