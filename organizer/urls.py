from django.conf.urls import url

from .views import tag_list, tag_detail

# see pg 148
urlpatterns = [
    url(r'^tag/$',
        tag_list,
        name='organizer_tag_list'
        ),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'
        ),
]

