from django.urls import path
from .views import home, CalculationView

urlpatterns = [
    path('', home, name='home'),
    path('api/calculate/', CalculationView.as_view(), name='calculation'),
]