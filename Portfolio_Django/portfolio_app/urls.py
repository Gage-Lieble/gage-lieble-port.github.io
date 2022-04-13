from django.urls import URLPattern, path
from . import views


app_name = 'portfolio_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('submitted/', views.submitted, name='submitted')
]

