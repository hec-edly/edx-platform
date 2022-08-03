"""
Configuration for ldap_auth support
"""
from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs, PluginSettings
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

class LDAPAuthConfig(AppConfig):
    """
    Configuration class for ldap_auth
    """
    name = 'openedx.features.hec_features.ldap_auth'
    plugin_app = {
        PluginSettings.CONFIG: {
            ProjectType.CMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings.common'},
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: 'settings.production'},
            },
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings.common'},
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: 'settings.production'},
            }
        }
    }
