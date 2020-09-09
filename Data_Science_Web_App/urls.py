from django.urls import path
from . import views

app_name = 'Data_Science_Web_App'
urlpatterns = [
    path('about_us/', views.AboutView.as_view(), name='AboutView'),
    path('average/', views.get_average, name='get_average'),
]
