from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import mark_safe
from wagtail.core import hooks
from wagtailcache.cache import clear_cache

from .models import AnalyticsSettings


class AnalyticsWarningPanel(object):
    name = 'analytics_warning_panel'
    order = 200

    def __init__(self, request):
        if not request.site:
            raise ValueError("Need an active site to show analytics warnings")
        self.request = request

    def render(self):
        instance = AnalyticsSettings.for_site(self.request.site)
        if not instance.google_analytics and not instance.google_tag_manager:
            return mark_safe(render_to_string('coop/analytics_warning.html', {
                'request': self.request,
            }))
        else:
            return ""


@hooks.register('construct_homepage_panels')
def analytics_warnings(request, panels):
    if settings.DEBUG:
        return
    try:
        analytics_panels = AnalyticsWarningPanel(request)
        panels.append(analytics_panels)
    except ValueError:
        pass


@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def clear_wagtailcache(request, page):
    if page.live:
        clear_cache()
