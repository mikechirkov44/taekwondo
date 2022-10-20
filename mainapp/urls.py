from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name


urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("history/", views.HistoryPageView.as_view(), name="history"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
    path("halls/", views.HallsPageView.as_view(), name="halls"),
    path("hall_of_fame/", views.Hall_of_FamePageView.as_view(), name="hall_of_fame"),
    path("trainers/", views.TrainersPageView.as_view(), name="trainers"),
    path("calendar/", views.CalendarPageView.as_view(), name="calendar"),
    path("video/", views.VideoPageView.as_view(), name="video"),
]
