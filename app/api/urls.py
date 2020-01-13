from django.urls import include, path

urlpatterns = [
    path('parent/', include('app.api.parent.urls')),

]