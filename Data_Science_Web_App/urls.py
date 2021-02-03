from django.urls import path
from . import views

app_name = 'Data_Science_Web_App'
urlpatterns = [
    path('about_us/', views.AboutView.as_view(), name='AboutView'),
    path('variable_stats/', views.variable_statistics, name='variable_statistics'),
    path('plot/', views.plot, name='plot'),
    path('main_page/', views.MainPageView.as_view(), name='MainPageView'),
    path('histogram/', views.histoplot, name='histoplot'),
    path('density_function/', views.density, name='density'),
    path('gaussian_smoothing/', views.gaussian, name='gaussian'),
    path('interpolation_NAN/', views.interpolation, name='interpolation'),
    path('transformation/', views.transformation, name='transformation'),
    path('packaging/', views.package, name='package'),
    path('visual/', views.visual, name = 'visual'),
    path('curve_fitter/', views.curve_fitter, name='curve_fitter'),
    path('log/', views.log, name='log'),
]
