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


class Hall(models.Model):
    placement = models.CharField(max_length=200, verbose_name="Расположение")

    def __str__(self):
        return f"{self.placement}"

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class Coach(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Имя")
    father_name = models.CharField(max_length=128, verbose_name="Отчество")
    last_name = models.CharField(
        max_length=128, verbose_name="Фамилия")
    hall = models.ManyToManyField(Hall, verbose_name="Залы")

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}.{self.father_name[0]}."

    class Meta:
        verbose_name = "Тренера"
        verbose_name_plural = "Тренеры"


class Contact(models.Model):
    """Определяем модель для формы обратной связи"""
    parents_name = models.CharField(
        max_length=200, verbose_name="ФИО родителя")
    child_name = models.CharField(max_length=50, verbose_name="ФИО ребенка")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст ребенка")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True,
        verbose_name="Номер телефона")
    hall = models.ForeignKey(
        Hall, on_delete=models.PROTECT, verbose_name="Залы")
    coach_name = models.ForeignKey(
        Coach, on_delete=models.PROTECT, verbose_name="Тренер")
    request_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата заявки")
    is_contacted = models.BooleanField(
        default=False, verbose_name="Связались")
    is_agreed = models.BooleanField(
        default=False, verbose_name="Согласие на обработку")

    def __str__(self) -> str:
        return f'{self.parents_name} - {self.phone_number}'

    class Meta():
        verbose_name_plural = "Контакты"
        verbose_name = "Контакт"


class Calendar(models.Model):
    """ Определяем модель для Календаря мероприятий"""
    title = models.CharField(
        max_length=256, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата мероприятия")
    duration = models.PositiveSmallIntegerField(
        verbose_name="Длительность мероприятия")
    city = models.CharField(max_length=64, verbose_name="Город")
    file_name = models.FileField(
        upload_to='uploads/', verbose_name="Файл с положением", default='uploads/default.html')
    in_archive = models.BooleanField(default=False, verbose_name="В архиве")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = "Соревнования"
        verbose_name = "Соревнование"


class Video(models.Model):
    """ Определяем модель для Видео"""
    title = models.CharField(
        max_length=256, verbose_name="Название мероприятия")
    date = models.DateField(verbose_name="Дата мероприятия")
    video_url = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Видео"
        verbose_name = "Видео"
