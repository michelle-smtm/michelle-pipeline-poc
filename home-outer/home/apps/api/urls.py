from django.urls import path
from .views import api_home, HelloWorldDetailAPIView, HelloWorldListCreateAPIView, HelloWorldUpdatAPIView, HelloWorldDeleteAPIView

urlpatterns = [
    path('<int:pk>/', HelloWorldDetailAPIView.as_view()),
    path('<int:pk>/update/', HelloWorldUpdatAPIView.as_view()),
    path('<int:pk>/delete/', HelloWorldDeleteAPIView.as_view()),
    path('', HelloWorldListCreateAPIView.as_view()),
    path('hello/', api_home)
]