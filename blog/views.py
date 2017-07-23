from django.shortcuts import (get_object_or_404, render)
from django.views.generic import View
from .models import Post

'''CBV- pg 155-160. Class based view- chap 5 introduced this form vs the function call below
# more detail to follow in chap 16.  Advantage of class vs function is more standard HTTP
interface and compliance w/ OOP standards.  most production designs will use CBV- see pg 158.
As of chap 5 some aspects
of CBV were backed out in book version, but will be re-implemented in later chaps.
'''
class PostList(View):
    def get(self, request):
        return render(
            request,
            'blog/post_list.html',
            {'post_list': Post.objects.all()}
        )


# function style call vs CBV (object) above
def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug
    )
    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )
