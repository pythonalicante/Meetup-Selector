from django.urls import path

from . import views

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="home"),
    path(
        "landingpage/collaborator/",
        views.CollaboratorListView.as_view(),
        name="collaborator_list",
    ),
    path(
        "landingpage/collaborator/<int:pk>/",
        views.CollaboratorDetailView.as_view(),
        name="collaborator",
    ),
]
