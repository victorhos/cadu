from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    url(
        r'^customers/',
        include(
            ('cadu.customers.urls', 'customers'),
            namespace='customers'
        )
    ),
    path('admin/', admin.site.urls),
]
