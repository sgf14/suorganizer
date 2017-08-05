from django.shortcuts import redirect, render
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