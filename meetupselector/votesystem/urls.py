from django.urls import path

from . import views

urlpatterns = [
    path('topic_proposal/', views.TopicProposalView.as_view(), name='topic_proposal'),
]
