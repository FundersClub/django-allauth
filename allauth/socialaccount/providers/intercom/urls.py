from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import IntercomProvider


urlpatterns = default_urlpatterns(IntercomProvider)
