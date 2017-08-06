from django.conf.urls import url

from .views import (
    NewsLinkCreate, NewsLinkUpdate, StartupCreate, TagCreate, TagUpdate, StartupUpdate,
    startup_detail, startup_list, tag_detail, tag_list,
    )

# see pg 148, this is supported by view.py, which then calls the html template file(s)
urlpatterns = [
    url(r'^startup/$',
        startup_list,
        name='organizer_startup_list'
        ),
    url(r'^startup/create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'
        ),
    url(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'
        ),
    url(r'^startup/(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'
        ),
    url(r'^tag/$',
        tag_list,
        name='organizer_tag_list'
        ),
    url(r'^tag/create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'
        ),
    # see pg 130 for regex pattern
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'
        ),
    url(r'^tag/(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update'
        ),
    url(r'^newslink/create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'
        ),
    url(r'^newslink/update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'
        ),
]

