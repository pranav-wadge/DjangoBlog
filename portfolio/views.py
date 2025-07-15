from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "portfolio/index.html"


class AboutView(TemplateView):
    template_name = "portfolio/about.html"


class ResumeView(TemplateView):
    template_name = 'portfolio/resume.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'


class ContactView(TemplateView):
    template_name = 'portfolio/contact.html'