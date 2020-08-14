from django.urls import path
from .views import (LoanUpdateView, LoanDetailView, LoanDeleteView)
from . import views


urlpatterns = [
    path('', views.home, name='loan-home'),
    path('loans/', views.LoanList, name='loan-list'),
    path('loan/<int:pk>/update/', LoanUpdateView.as_view(), name='loan-update'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('loan/<int:pk>/delete/', LoanDeleteView.as_view(), name='loan-delete'),
    path('create/', views.NewLoan, name='loan-create'),
]
