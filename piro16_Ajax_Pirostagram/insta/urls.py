from django.urls import path
from insta import views

app_name = 'insta'

urlpatterns = [
    path('', views.home, name='home'),
    path('like/', views.like, name="like")
]