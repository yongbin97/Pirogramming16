from django.urls import path, include
from . import views

app_name = "SWIDEA"

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/new/', views.idea_new, name="idea_new"),
    path('idea/<int:pk>/update/', views.idea_update, name='idea_update'),
    path('idea/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('dev/list/', views.dev_list, name='dev_list'),
    path('dev/<int:pk>/', views.dev_detail, name='dev_detail'),
    path('dev/new/', views.dev_new, name="dev_new"),
    path('dev/<int:pk>/update/', views.dev_update, name='dev_update'),
    path('dev/<int:pk>/delete/', views.dev_delete, name='dev_delete'),
    path('idea/plus/', views.idea_plus, name='idea_plus'),
    path('idea/minus/', views.idea_minus, name='idea_minus'),
]