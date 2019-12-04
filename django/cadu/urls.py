from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from cadu.customers import views

urlpatterns = [
    url(
        r'^customer/(?P<pk>\d+)/',
        views.CustomerRetrieveUpdateDestroyViews.as_view(),
        name='customers_retrive_update'
    ),
    url(
        r'^customer/',
        views.CustomerCreateViews.as_view(),
        name='customers_create'
    ),
    url(
        r'^customers/',
        views.CustomerListViews.as_view(),
        name='customers_list'
    ),
    path('admin/', admin.site.urls),
]
