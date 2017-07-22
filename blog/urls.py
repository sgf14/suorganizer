from django.conf.urls import url
from .views import post_detail, post_list

urlpatterns = [
    url(r'^$',
        post_list,
        name='blog_post_list'
        ),
    url(r'^(?P<year>\d{4})/'  # NOTE-no commas. one long string broken into parts
        r'(?P<month>\d{1,2})/'  # compare to organizer tag detail
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'
        ),
]
