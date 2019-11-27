from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CustomerViews.as_view(), name='list_create'),
]
