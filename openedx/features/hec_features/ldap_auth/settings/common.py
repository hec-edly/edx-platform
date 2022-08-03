
"""Common settings for LDAP Auth"""
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

def plugin_settings(settings):
    """
    Common settings for LDAP Auth
    """
    # settings for ldap
    settings.AUTH_LDAP_SERVER_URI = 'pern.pk'
    settings.AUTH_LDAP_BIND_DN = 'cn=moocs.edx,dc=example,dc=com'
    settings.AUTH_LDAP_BIND_PASSWORD = 'Moocs7890'
    settings.AUTH_LDAP_USER_SEARCH = LDAPSearch('dc=example,dc=com',ldap.SCOPE_SUBTREE, '(uid=%(user)s)')

    settings.AUTH_LDAP_USER_ATTR_MAP = {
            "first_name": "givenName",
            "last_name": "sn",
            "email": "mail",
            "username": "uid",
            "password": "userPassword",
    }

    settings.AUTH_LDAP_ALWAYS_UPDATE_USER = True
    settings.AUTH_LDAP_CACHE_TIMEOUT = 3600

    settings.AUTHENTICATION_BACKENDS = ['django_auth_ldap.backend.LDAPBackend'] + settings.AUTHENTICATION_BACKENDS
