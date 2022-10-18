from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.generic import TemplateView
from django.shortcuts import render


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["parents_name"]} Телефон отправителя: {data["phone_number"]}'
        email(subject, data['phone_number'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
    send_mail(subject,
              f'Новая заявка  c сайта. Просьба позвонить по телефону {content}',
              'ya.mikechirkov@yandex.ru',
              ['ya.mikechirkov@yandex.ru']
              )

# Функция, которая вернет сообщение в случае успешного заполнения формы


def success(request):
    return HttpResponse('Письмо отправлено!')


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class AboutPageView(TemplateView):
    template_name = "mainapp/about.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class HistoryPageView(TemplateView):
    template_name = "mainapp/history.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"


class HallsPageView(TemplateView):
    template_name = "mainapp/halls.html"


class Hall_of_FamePageView(TemplateView):
    template_name = "mainapp/hall_of_fame.html"


class TrainersPageView(TemplateView):
    template_name = "mainapp/trainers.html"


class CalendarPageView(TemplateView):
    template_name = "mainapp/calendar.html"


class VideoPageView(TemplateView):
    template_name = "mainapp/video.html"


def page_not_found(request, exception):
    return render(request, 'mainapp/not_found.html', status=404)
