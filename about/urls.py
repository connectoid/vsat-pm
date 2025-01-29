from django.urls import path

from .views import AboutView

app_name = 'about'

urlpatterns = [
    path(
        '',
        AboutView.as_view(template_name='about/about.html'),
        name='about'
    ),
]
