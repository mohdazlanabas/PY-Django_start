from django.urls import path
from . import views
import debug_toolbar  # Django Debug Toolbar
from django.urls import include

urlpatterns = [
    path("", views.index, name="index"),
]
