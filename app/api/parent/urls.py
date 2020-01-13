from django.urls import include, path

from app.api.parent import views

urlpatterns = [
    path('create', views.ParentCreateAPIView.as_view(), name='api-parent-create'),
    path('update/<int:id>', views.ParentUpdateAPIView.as_view(), name='api-parent-update'),
    path('destroy/<int:id>', views.ParentDestroyAPIView.as_view(), name='api-parent-destroy'),

]