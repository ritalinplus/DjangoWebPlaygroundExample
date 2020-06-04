from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "core/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Test web Playground'
    #     return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Test web Playground'})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"

