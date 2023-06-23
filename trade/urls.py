from django.urls import path
from . import views


urlpatterns = [
    path('',  views.Home.as_view(), name="home"),
    path('login/',  views.Login.as_view(), name="login"),
    path('logout/',  views.Logout.as_view(), name="logout"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('dashboard/<int:pk>/', views.Dashboard.as_view(), name="dashboard-key"),
]
