from django.urls import path
from . import views
from .views import PrettifyNumberView

urlpatterns = [
    path('', views.prettify, name='prettify'),
    path('<str:number>/', PrettifyNumberView.as_view(), name='prettify_number'),
]
