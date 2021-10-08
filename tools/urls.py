from django.urls import path
from tools.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
