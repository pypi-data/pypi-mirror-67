from django.conf import settings

if 'reversion' in settings.INSTALLED_APPS:  # pragma: no cover
    from reversion.admin import VersionAdmin as BaseModelAdmin
else:
    from django.contrib.admin import ModelAdmin as BaseModelAdmin


class BaseAdmin(BaseModelAdmin):
    history_latest_first = True
