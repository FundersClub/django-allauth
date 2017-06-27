from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class IntercomAccount(ProviderAccount):
    pass


class IntercomProvider(OAuth2Provider):
    id = 'intercom'
    name = 'Intercom'
    account_class = IntercomAccount

provider_classes = [IntercomProvider]
