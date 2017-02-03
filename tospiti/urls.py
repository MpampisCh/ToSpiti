from django.conf.urls import url
from . import views

app_name = 'tospiti'

urlpatterns = [
    # /tospiti/
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    # /tospiti/properties/
    url(r'^properties/$', views.IndexView.as_view(), name='index'),
    #/tospiti/properties/<prop_category>/
    url(r'^properties/category$',views.PropertyDetailList.as_view(), name='propertycategories'),
    # /tospiti/to/<prop_genre>/
    url(r'^properties/genre$',views.PropertyGenreList.as_view(), name='propertygenres'),
    # /tospiti/properties/<id_prop>/
    url(r'^properties/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /tospiti/agents/
    url(r'^agents/$', views.AgentsView.as_view(), name='agents'),
    # /tospiti/proppictures/
    url(r'^proppictures/$', views.PropPicturesView.as_view(), name='proppictures'),
]