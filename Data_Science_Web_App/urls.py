from django.urls import path
from . import views

app_name = 'Data_Science_Web_App'
urlpatterns = [
    path('about_us/', views.AboutView.as_view(), name='AboutView'),
    path('average/', views.get_average, name='get_average'),
    path('plot/', views.plot, name='plot'),
    path('main_page/', views.MainPageView.as_view(), name='MainPageView'),
    path('histogram/', views.histoplot, name='histoplot'),
    path('density_function/', views.density, name='density'),
    path('gaussian_smoothing/', views.gaussian, name='gaussian'),
    path('interpolation_NAN/', views.interpolation, name='interpolation'),
    path('transformation/', views.transformation, name='transformation'),
]
