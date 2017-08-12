from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
# Abstract classes for common inheritance functions


class ObjectCreateMixin:
    # this abstract (..Mixin pythonic convention) class used for
    # standard http get/post code- called by views.  chap 9 pg 255
    form_class = None
    template_name = ''

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


class ObjectUpdateMixin:
    form_class = None
    model = None
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model,
            slug__iexact=slug
        )
        context = {
            'form': self.form_class(instance=obj),
            self.model.__name__.lower(): obj,
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model,
            slug__iexact=slug
        )
        bound_form = self.form_class(request.POST, instance=obj)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                self.model.__name__.lower(): obj,
            }
            return render(
                request,
                self.template_name,
                context
            )


class ObjectDeleteMixin:
    model = None
    success_url = ''
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model,
            slug__iexact=slug
        )
        context = {
            self.model.__name__.lower(): obj,
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request, slug):
        # note even though you are not using 'request' var above in the code below you have to have it
        # because it will be passed
        obj = get_object_or_404(
            self.model,
            slug__iexact=slug
        )
        obj.delete()
        return HttpResponseRedirect(
            self.success_url
        )


