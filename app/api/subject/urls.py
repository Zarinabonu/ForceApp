from django.urls import path

from app.api.subject import views

urlpatterns = [
    path('create', views.SubjectCreateAPIView.as_view(), name='api-subject-create'),
    path('destroy/<int:id>', views.SubjectDestroyAPIView.as_view(), name='api-subject-destroy'),

]