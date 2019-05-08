from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_recipe, name="cookbook"),
    path("plan/", views.plan, name="plan"),
]
