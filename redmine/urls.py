from django.conf.urls import url
from redmine import views

urlpatterns = [
    url(r'^', views.HomePageView.as_view()),
]
