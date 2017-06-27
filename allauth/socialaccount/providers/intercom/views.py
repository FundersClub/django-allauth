from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from ..adapter import get_adapter
from .provider import IntercomProvider


class IntercomOAuth2Adapter(OAuth2Adapter):
    provider_id = IntercomProvider.id
    access_token_url = 'https://api.intercom.io/auth/eagle/token'
    authorize_url = 'https://app.intercom.io/oauth'

    def complete_login(self, request, app, token, **kwargs):
        # This is a hack until intercom lets us know the profile url to use
        try:
            response = {}

            from allauth.socialaccount.models import SocialLogin, SocialAccount

            adapter = get_adapter(request)
            uid = self.extract_uid(response)
            extra_data = self.extract_extra_data(response)
            common_fields = self.extract_common_fields(response)
            socialaccount = SocialAccount(extra_data=extra_data,
                                          uid=uid,
                                          provider=self.id)
            email_addresses = self.extract_email_addresses(response)
            self.cleanup_email_addresses(common_fields.get('email'),
                                         email_addresses)
            sociallogin = SocialLogin(account=socialaccount,
                                      email_addresses=email_addresses)
            user = sociallogin.user = adapter.new_user(request, sociallogin)
            user.set_unusable_password()
            adapter.populate_user(request, sociallogin, common_fields)
            return sociallogin
        except Exception as e:
            raise e

oauth2_login = OAuth2LoginView.adapter_view(IntercomOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(IntercomOAuth2Adapter)
