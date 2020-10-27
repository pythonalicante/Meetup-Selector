from django.urls import path

from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='home'),
]
