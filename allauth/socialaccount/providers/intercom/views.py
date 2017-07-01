import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import IntercomProvider


class IntercomOAuth2Adapter(OAuth2Adapter):
    provider_id = IntercomProvider.id
    access_token_url = 'https://api.intercom.io/auth/eagle/token'
    authorize_url = 'https://app.intercom.io/oauth'
    profile_url = 'https://api.intercom.io/me'

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'Accept': 'application/json',
                                    'Authorization': 'Bearer {0}'.format(token.token)})
        return self.get_provider().sociallogin_from_response(request, resp.json())

oauth2_login = OAuth2LoginView.adapter_view(IntercomOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(IntercomOAuth2Adapter)
