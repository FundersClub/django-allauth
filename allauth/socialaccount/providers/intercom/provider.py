from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class IntercomAccount(ProviderAccount):
    pass


class IntercomProvider(OAuth2Provider):
    id = 'intercom'
    name = 'Intercom'
    account_class = IntercomAccount

    def extract_uid(self, data):
        # This is a hack until intercom lets us know what API to use
        return str(data['token'])


provider_classes = [IntercomProvider]
