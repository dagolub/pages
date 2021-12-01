from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:page_url>', views.view, name='view'),
]