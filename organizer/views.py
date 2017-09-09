from django.shortcuts import (get_object_or_404, redirect, render)
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import (EmptyPage, PageNotAnInteger, Paginator)
from django.views.generic import View
from .models import NewsLink, Startup, Tag
from .forms import NewsLinkForm, StartupForm, TagForm
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin

# orig startup_list function version
'''def startup_list(request):
    # see pg 149 and 150- started with tags first in book example
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()}
    )
'''
# replaced w/ StartupList class (CBV) version in chap 14- pagination, pg 338
class StartupList(View):
    page_kwarg = 'page'
    paginate_by = 5  # 5 items per page
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(
            startups, self.paginate_by
        )
        page_number = request.GET.get(self.page_kwarg)

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number()
            )
        else:
            prev_url = None

        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number()
            )
        else:
            next_url = None

        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'startup_list': page}
        return render(
            request,
            self.template_name,
            context
        )


def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug
    )
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup}
    )


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()}
    )


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag}
    )


def tag_create(request):
    # CRUD ops.  This is option 1- a function.  Chap 9, pg 246. this is not called, but left in
    # place for demonstration purposes
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else: # empty or invalid data
            form = TagForm()
        return render(
            request,
            'organizer/tag_form.html',
            {'form': form}
        )


'''Note classes below vs functions above.  either can be used
as book goes along classes (CBV- Class based Views) are more frequently used. as they are more flexible.
'''

class TagCreate(View):
    # this is option 2- Ch 9.  A class (CBV) and is the more standard practice- see pg 238-240 and 247
    form_class = TagForm
    template_name = 'organizer/tag_form.html'
    # note ch9 pg 255- normally ObjectCreateMixin would be inherited for below - as w/ following classes
    # but code left in as a demo for tag_create above- to see comparison
    # this left in  only as learning example- would not do this in PROD code

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()}
        )

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form}
            )


class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = 'organizer/tag_form_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')
    template_name = 'organizer/tag_confirm_delete.html'


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


class StartupUpdate(ObjectUpdateMixin, View):
    form_class = StartupForm
    model = Startup
    template_name = 'organizer/startup_form_update.html'


class StartupDelete(ObjectDeleteMixin, View):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    template_name = 'organizer/startup_confirm_delete.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = ('organizer/newslink_form_update.html')

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink,
            pk=pk
        )
        context = {
            'form': self.form_class(instance=newslink),
            'newslink': newslink,
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink,
            pk=pk
        )
        bound_form = self.form_class(
            request.POST,
            instance=newslink
        )
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': bound_form,
                'newslink': newslink,
            }
            return render(
                request,
                self.template_name,
                context
            )


class NewsLinkDelete(View):
    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink,
            pk=pk
        )
        return render(
            request,
            'organizer/newslink_confirm_delete.html',
            {'newslink': newslink}
        )

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink,
            pk=pk
        )
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)
