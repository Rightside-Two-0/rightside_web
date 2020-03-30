from django.urls import path
from pages.views import DashboardPageView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
]
