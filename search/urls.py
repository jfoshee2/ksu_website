from django.conf.urls import url
from . import views

#This is a namespace
app_name = 'search'

urlpatterns = [
    #This is the homepage of the search app
    #/search/      ~this is what index will be referencing
    url(r'^$', views.index, name='index'),



    # /Search/<Album id>/    ~this is what detail will be referencing
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),

    # /Search/<Album id>/add_to_cart    ~this is what detail will be referencing
    url(r'^(?P<book_id>[0-9]+)/add_to_cart/$', views.detail, name='add_to_cart'),
]


