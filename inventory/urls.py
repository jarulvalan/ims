from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<product_id>[0-9]+)$', detail, name="detail"),
]
