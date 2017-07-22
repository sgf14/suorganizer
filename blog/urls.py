from django.conf.urls import url
from .views import post_detail, PostList

urlpatterns = [
    url(r'^$',
        PostList.as_view(),
        name='blog_post_list'
        ),
    url(r'^(?P<year>\d{4})/'  # NOTE-no commas. one long string broken into parts
        r'(?P<month>\d{1,2})/'  # compare to organizer tag detail
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'
        ),
]
