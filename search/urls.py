from django.conf.urls import url
from . import views


urlpatterns = [
    #This is the homepage of the search app
    #/search/
    url(r'^$', views.index, name='index'),

    # /Search/:id/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
