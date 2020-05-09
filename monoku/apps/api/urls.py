from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('regions/', views.RegionsCountry.as_view(), name='regions_country')
]
