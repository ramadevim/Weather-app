from django.urls import path
from weatherapp import views

app_name='weatherapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<city_name>/',views.delete_city,name='delete_city')
]