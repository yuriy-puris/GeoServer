from django.urls import path

from .views import AddressView, CoordinatesView, ParseLocationView, TestDomainView

urlpatterns = [
  path('address', AddressView.as_view(), name='address'),
  path('coordinates', CoordinatesView.as_view(), name='coordinate'),
  path('post_location', ParseLocationView.as_view(), name='post_location'),
  path('test', TestDomainView.as_view(), name='test'),
]
