from django.urls import path
from hotel import views
urlpatterns=[
    path('menu',views.home,name='menu')
]