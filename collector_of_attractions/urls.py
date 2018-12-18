from django.conf.urls import url

from .views import (
    AttractionDetailView,
    AttractionListView,
    CategoryListView,
    AttractionCreateView
)


urlpatterns = [

    url(r'^$', AttractionListView.as_view(), name='attractions_list'),
    url(r'^create/$', AttractionCreateView.as_view(), name='create'),
    url(r'^(?P<cat>\w+)/$', CategoryListView.as_view(), name='category_list'),
    url(r'^(?P<cat>\w+)/(?P<slug>[\w-]+)/$', AttractionDetailView.as_view(), name='detail_view'),


]