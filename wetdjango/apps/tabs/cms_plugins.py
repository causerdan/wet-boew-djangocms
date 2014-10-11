# -*- coding: utf-8 -*-

from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TabsPluginModel

class  TabsPlugin(CMSPluginBase):
	name = U'Tabs'
	model = TabsPluginModel
	render_template = "tabs/_tabs_plugin.html"
	text_enabled = True

	def render(self, context, instance, placeholder):
			context['instance'] = instance
			return context

	def icon_src(self, instance):
		return settings.STATIC_URL + 'tabs/images/tabs_icon.png'

	def icon_alt(self, instance):
		return u'Tabs: %s' % instance

plugin_pool.register_plugin(TabsPlugin)


