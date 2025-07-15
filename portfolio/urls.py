from django.urls import path

from .views import IndexView, AboutView, ResumeView, PortfolioView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name="about"),
    path('resume', ResumeView.as_view(), name="resume"),
    path('portfolio', PortfolioView.as_view(), name="portfolio"),
    path('contact', ContactView.as_view(), name="contact"),
]