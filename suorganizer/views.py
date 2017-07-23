from django.shortcuts import redirect
# site wide views.  pg 165- redirect homepage to blog list/  w/o this
# the base website dir gives a 404 error.  use this when there is not a standalone
# homepage- use it to redirect to an existing app- blog list in this case


def redirect_root(request):
    # the webpage version
    # return redirect('/blog/')

    # the name version- both redirect to the same place, pg 166
    return redirect('blog_post_list')

