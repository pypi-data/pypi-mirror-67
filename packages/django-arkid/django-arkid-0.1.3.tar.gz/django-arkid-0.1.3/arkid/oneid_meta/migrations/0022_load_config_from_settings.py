from sys import _getframe

from django.db import migrations, models
from django.contrib.sites.models import Site
from django.conf import settings

from ...common.setup_utils import NotConfiguredException, validate_attr


def load_config_from_settings(apps, schema_editor):

    CompanyConfig = apps.get_model('oneid_meta', 'CompanyConfig')
    DingConfig = apps.get_model('oneid_meta', 'DingConfig')
    Site = apps.get_model('sites', 'Site')
    validate_attr(_getframe().f_code.co_filename, _getframe().f_code.co_name, _getframe().f_lineno,
                  'SITE_ID')
    site, _ = Site.objects.get_or_create(id=settings.SITE_ID)
    ding_config, _ = DingConfig.objects.get_or_create(site=site)
    company_config, _ = CompanyConfig.objects.get_or_create(site=site)

    validate_attr(_getframe().f_code.co_filename, _getframe().f_code.co_name, _getframe().f_lineno, 'TESTING')

    if not settings.TESTING:
        ding_config.app_key = getattr(settings, 'DINGDING_APP_KEY', '')
        ding_config.app_secret = getattr(settings, 'DINGDING_APP_SECRET', '')
        ding_config.save()


class Migration(migrations.Migration):
    '''
    load config from settings
    '''
    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('oneid_meta', '0021_auto_20190424_1524'),
    ]

    operations = [
        migrations.RunPython(load_config_from_settings),
    ]
