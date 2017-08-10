from django.conf.urls import url
from hear1.views import *

urlpatterns = [
    
    url(r'^index/$', HomeView.as_view(), name="index"),
    url(r'^email/$', EmailView.as_view(), name="email"),
    url(r'^text/$', TextView.as_view(), name="text"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^test/$', TestView.as_view(), name="test"),
    url(r'^index/(?P<slug>[a-z, A-Z, ' ']+)/$', HomeView.as_view(), name="index"),
    # url(r'^news_list/$', News.as_view(), name="news_list"),
]
