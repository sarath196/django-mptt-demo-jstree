from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static 

from landing.views import RenderLanding
from . import views


urlpatterns = [
                url(r'^$', RenderLanding.as_view(), name='render_landing'),
                 ]