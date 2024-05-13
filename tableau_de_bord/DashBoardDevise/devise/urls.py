from django.urls import path

from .views import dashboard, page_d_acceuill

urlpatterns = [
    path('days=<int:days_range>&currencies=<str:currencies>&affichage=<str:affichage>', dashboard, name="home"),
    path('', page_d_acceuill)
]