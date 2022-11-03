from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig
from django.views.decorators.cache import cache_page


app_name = MainappConfig.name


urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("history/", views.HistoryPageView.as_view(), name="history"),
    path("schedule/", views.SchedulePageView.as_view(), name="schedule"),
    path("news/", cache_page(60*5)(views.NewsListView.as_view()),
         name="news"),  # cache 5 min
    path("form/", views.ContactCreate.as_view(), name="contact_page"),
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
    path("halls/", views.HallsPageView.as_view(), name="halls"),
    path("hall_of_fame/", views.Hall_of_FamePageView.as_view(), name="hall_of_fame"),
    path("trainers/", views.TrainersPageView.as_view(), name="trainers"),
    path("calendar/",  cache_page(60*5)
         (views.CalendarPageView.as_view()), name="calendar"),
    path("success/", views.SuccessPageView.as_view(), name="success_page"),
    path("video/",  cache_page(60*5)(views.VideoPageView.as_view()), name="video"),
]
