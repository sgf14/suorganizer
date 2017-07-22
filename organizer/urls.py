from django.conf.urls import url

from .views import (
    startup_detail, startup_list, tag_list, tag_detail
    )

# see pg 148, this is supported by view.py, which then calls the html template file(s)
urlpatterns = [
    url(r'^startup/$',
        startup_list,
        name='organizer_startup_list'
        ),
    url(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'
        ),
    url(r'^tag/$',
        tag_list,
        name='organizer_tag_list'
        ),
    # see pg 130 for regex pattern
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'
        ),
]

