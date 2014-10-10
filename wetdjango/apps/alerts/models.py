# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin

class AlertsPluginModel(CMSPlugin):

	alert_type = models.CharField('Alert Type',
		blank=False,
		default='warning',
		help_text=u'Please Enter the class tag of the alert',
		max_length=32,
		)

	alert_title = models.CharField('Alert Title',
		blank=False,
		default='',
		help_text=u'Please Enter the title of the alert',
		max_length=64,
		)

	alert_msg = models.CharField('Alert Message',
		blank=False,
		default='',
		help_text=u'Please Enter the message of the alert',
		max_length=225,
		)

	def __unicode__(self):
		return u'%s:%s:%s' % (self.alert_type, self.alert_title, self.alert_msg, )