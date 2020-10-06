from django.urls import path

from . import views

urlpatterns = [
    path('topic_proposal/', views.topic_proposal, name='topic_proposal'),
]
