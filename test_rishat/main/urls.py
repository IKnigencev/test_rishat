from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('buy/<int:id>/', views.buy_view, name='buy'),
    path('item/<int:id>/', views.item_profile, name='item'),
    path('', views.index, name='index')
]
