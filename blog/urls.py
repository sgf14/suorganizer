from django.conf.urls import url
from .views import post_detail, PostCreate, PostList, PostUpdate, PostDelete

urlpatterns = [
    url(r'^$',
        PostList.as_view(),
        name='blog_post_list',
        ),
    url(r'^create/$',
        PostCreate.as_view(),
        name='blog_post_create'
        ),
    url(r'^(?P<year>\d{4})/'  # NOTE-no commas. one long string broken into parts
        r'(?P<month>\d{1,2})/'  # compare to organizer tag detail
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail',
        ),
    url(r'^(?P<year>\d{4})/'  # Note- similar to above, no comma for these is correct
        r'(?P<month>\d{1,2})/'  # need single URL string
        r'(?P<slug>[\w\-]+)/'
        r'update/$',
        PostUpdate.as_view(),
        name='blog_post_update',
        ),
    url(r'^(?P<year>\d{4})/'  # Note- similar to above, no comma for these is correct
        r'(?P<month>\d{1,2})/'  # need single URL string
        r'(?P<slug>[\w\-]+)/'
        r'delete/$',
        PostDelete.as_view(),
        name='blog_post_delete',
        ),
]
