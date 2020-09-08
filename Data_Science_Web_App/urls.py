from django.urls import path
from . import views
urlpatterns = [
    path('about_us/', views.AboutView.as_view(), name='AboutView'),
]
