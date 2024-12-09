from django.urls import path
from . import views
from .views import MenuItemDetail, AboutDetail

urlpatterns = [
    path("", views.MenuList.as_view(), name="home"),
    path('item/<int:pk>/', MenuItemDetail.as_view(), name='menu_item'),
    path("/about", AboutDetail.as_view(), name="about")
]