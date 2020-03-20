from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('hadiths/',views.hadiths, name='hadiths'),
    path('videos/',views.videos, name='videos'),
    path('coronaintheworld/',views.coronaintheworld, name='coronaintheworld'),
    path('statistics/', views.statistics, name='statistics'),

]