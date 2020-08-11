from django.urls import path
from .views import (
    LoanCreateView,
    LoanDetailView)
from . import views


urlpatterns = [
    path('', views.home, name='loan-home'),
    path('about/', views.about, name='loan-about'),
    path('loan/new/', LoanCreateView.as_view(), name='loan-create'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
]
