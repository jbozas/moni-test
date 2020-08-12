from django.urls import path
from .views import (LoanDetailView)
from . import views


urlpatterns = [
    path('', views.home, name='loan-home'),
    path('about/', views.about, name='loan-about'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('create/', views.NewLoan, name='loan-create'),
]
