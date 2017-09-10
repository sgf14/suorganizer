from django.conf.urls import url

from .views import (
    NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete,
    StartupCreate, StartupUpdate, StartupDelete,
    TagCreate, TagUpdate, TagDelete,
    StartupList,
    TagList, TagPageList,
    startup_detail, tag_detail, # tag_list,  startup_list,
    )

# see pg 148, this is supported by view.py, which then calls the html template file(s)
# note: later on- 09/03/17- chap 11, pg 308 refactored this app by splitting the urls into a separate
# url module (folder,like templates).  but I chose not to implement this in my app
# it is realtively simple to implement if you wanted to later.  in a larger prod app
# you would want to model this sort of url module
urlpatterns = [
    url(r'^startup/$', # note in book, upon cbv this changed from r'^startup/$' to r'^$', pg 338, but either
        # seems to work
        # startup_list, # original function
        StartupList.as_view(), # new CBV
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
    url(r'^startup/(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(),
        name='organizer_startup_delete'
        ),
    url(r'^tag/$',  # pagination, url ver 1- xx/tag/
        TagList.as_view(),
        name='organizer_tag_list'
        ),
    url(r'^tag/(?P<page_number>\d+)/$',  # pagination- url ver 2- xx/tag/2/.  see pg 349 for regex pattern
        TagPageList.as_view(),
        name='organizer_tag_page'
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
    url(r'^tag/(?P<slug>[\w\-]+)/delete/$',
        TagDelete.as_view(),
        name='organizer_tag_delete'
        ),
    url(r'^newslink/create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'
        ),
    url(r'^newslink/update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'
        ),
    url(r'^newslink/delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'
        ),
]

