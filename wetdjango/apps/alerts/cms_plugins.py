# -*- coding: utf-8 -*-

from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import AlertsPluginModel

class  AlertsPlugin(CMSPluginBase):
	name = U'Alerts'
	model = AlertsPluginModel
	render_template = "alerts/_alerts_plugin.html"
	text_enabled = True

	def render(self, context, instance, placeholder):

			context['instance'] = instance

			return context

	def icon_src(self, instance):
		return settings.STATIC_URL + 'alerts/images/alert_plugin_icon.png'

	def icon_alt(self, instance):
		return u'Alert: %s' % instance

plugin_pool.register_plugin(AlertsPlugin)


