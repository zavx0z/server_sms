from django.urls import path

from bandwidth import views

urlpatterns = [
    path('', views.index, name='index'),
]