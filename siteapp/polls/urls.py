from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poll_form/', views.poll_form, name='poll_form'),
    path('submit_poll/', views.submit_poll, name='submit_poll'),
    path('result/', views.show_result, name='show_result'),
]
