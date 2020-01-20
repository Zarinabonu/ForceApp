from django.urls import path

from app.api.statistic import views

urlpatterns = [
    path('list', views.StatisticListAPIView.as_view(), name='api-statistic-list'),

]