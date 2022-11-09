from django.views.generic import CreateView, TemplateView, ListView

from .models import Contact, HallOfFame, News, Video, Calendar
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm

from django.shortcuts import render, get_object_or_404
from mainapp import models as mainapp_models


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('mainapp:success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Новая заявка с сайта. От: {data["parents_name"]}. Телефон: {data["phone_number"]}'
        email(subject, data['phone_number'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
    send_mail(subject,
              f'Поступила новая заявка c сайта. Просьба позвонить по телефону {content}',
              'ya.mikechirkov@yandex.ru',
              ['ya.mikechirkov@yandex.ru', 'mail@taekwondo44.ru']
              )

# Функция, которая вернет сообщение в случае успешного заполнения формы


def success(request):
    return HttpResponse('Письмо отправлено!')


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['news_qs'] = mainapp_models.News.objects.filter(deleted=False)[
            :3]
        return context


class AboutPageView(TemplateView):
    template_name = "mainapp/about.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class HistoryPageView(TemplateView):
    template_name = "mainapp/history.html"


class NewsListView(ListView):
    model = News
    template_name = "mainapp/news.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['news_qs'] = mainapp_models.News.objects.filter(deleted=False)
        return context


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None,  **kwargs):
        # Get all previous data
        context = super().get_context_data(pk=pk, **kwargs)
        # Create your own data
        context['news_object'] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class HallsPageView(TemplateView):
    template_name = "mainapp/halls.html"


class Hall_of_FamePageView(ListView):
    model = HallOfFame
    paginate_by = 2
    template_name = "mainapp/hall_of_fame.html"

    def get_context_data(self, pk=None,  **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['halloffame_qs'] = mainapp_models.HallOfFame.objects.all()
        return context


class TrainersPageView(TemplateView):
    template_name = "mainapp/trainers.html"


class SchedulePageView(TemplateView):
    template_name = "mainapp/schedule.html"


class SuccessPageView(TemplateView):
    template_name = "mainapp/success.html"


class CalendarPageView(ListView):
    model = Calendar
    template_name = "mainapp/calendar.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['calendar_qs'] = mainapp_models.Calendar.objects.all()
        return context


class VideoPageView(ListView):
    model = Video
    template_name = "mainapp/video.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['video_qs'] = mainapp_models.Video.objects.all()
        return context


def page_not_found(request, exception):
    return render(request, 'mainapp/not_found.html', status=404)
