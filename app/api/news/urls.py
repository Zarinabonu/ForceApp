from django.urls import path

from app.api.news import views

urlpatterns = [
    path('list/', views.NewsListAPIView.as_view(), name='api-news-list'),
]