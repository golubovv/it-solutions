from django.urls import path
from ticker import views

urlpatterns = [
    path('', views.TickerCreateView.as_view(), name='create_ticker'),
    path('create_font', views.FontCreateView.as_view(), name='create_font'),
    path('download/<int:pk>', views.download, name='download_ticker')
]