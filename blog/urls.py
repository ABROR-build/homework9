from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('detailed/<int:pk>/', views.BlogDetail.as_view(), name='detailed')
]
