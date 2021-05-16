from django.views.generic import TemplateView

from dbloyalty.models import Member


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members_count'] = Member.objects.count()
        return context


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
