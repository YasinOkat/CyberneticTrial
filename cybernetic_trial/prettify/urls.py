from django.urls import path
from . import views
from .views import PrettifyNumber

urlpatterns = [
    path('', views.prettify, name='prettify'),
    path('<str:input_num>/', PrettifyNumber.as_view(), name='prettify_number'),
]
