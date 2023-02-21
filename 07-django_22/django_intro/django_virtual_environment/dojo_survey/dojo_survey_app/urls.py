from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('dojo_result', views.dojo_form)
]