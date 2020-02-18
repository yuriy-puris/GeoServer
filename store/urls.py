from django.urls import path

from .views import ShopView, AddressView, CoordinatesView, ParseLocationView

urlpatterns = [
  path('shop', ShopView.as_view(), name='shop'),
  path('address', AddressView.as_view(), name='address'),
  path('coordinates', CoordinatesView.as_view(), name='coordinate'),
  path('post_location', ParseLocationView.as_view(), name='post_location'),
]
