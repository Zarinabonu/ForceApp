from django.urls import path

from app.api.mark import views

urlpatterns = [
    path('create', views.MarkCreateAPIView.as_view(), name='api-mark-create'),
    path('update/<int:id>', views.MarkUpdateAPIView.as_view(), name='api-mark-update'),
    path('destroy/<int:id>', views.MarkDestroyAPIView.as_view(), name='api-mark-destroy'),

]