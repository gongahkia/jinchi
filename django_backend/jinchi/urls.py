from django.urls import path
from .views import AnimationAPI

urlpatterns = [
    path("", AnimationAPI.as_view(), name="animate"),
]
