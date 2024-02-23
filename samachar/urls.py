from django.urls import path
from . import views

urlpatterns = [
    path('', views.YourView.as_view(), name='index'),
    path('add_news/', views.YourView.add_news, name='add_news'),
    path('detail/<int:id>/', views.YourView.detail, name='detail'),
]
