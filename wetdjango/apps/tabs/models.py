# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin

class TabsPluginModel(CMSPlugin):

	tab1_title = models.CharField('Tab Title 1',
		blank=False,
		default='',
		help_text=u'Please enter the Title of tab 1',
		max_length=32,
		) 
	tab1_slug = models.SlugField('Tab Slug 1',
		blank=False,
		default='',
		help_text=u'Please enter the Slug of tab 1',
		max_length=32,
		) 
	tab1_text = models.TextField('Tab 1 Text',
		blank=False,
		default='',
		)
	tab2_title = models.CharField('Tab Title 2',
		blank=True,
		default='',
		help_text=u'Please enter the Title of tab 1',
		max_length=32,
		)
	tab2_slug = models.SlugField('Tab Slug 2',
		blank=True,
		default='',
		help_text=u'Please enter the Slug of tab 2',
		max_length=32,
		) 
	tab2_text = models.TextField('Tab 2 Text',
		blank=True,
		default='',
		)
	tab3_title = models.CharField('Tab Title 3',
		blank=True,
		default='',
		help_text=u'Please enter the Title of tab 3',
		max_length=32,
		)
	tab3_slug = models.SlugField('Tab Slug 3',
		blank=True,
		default='',
		help_text=u'Please enter the Slug of tab 3',
		max_length=32,
		) 
	tab3_text = models.TextField('Tab 3 Text',
		blank=True,
		default='',
		)
	tab4_title = models.CharField('Tab Title 4',
		blank=True,
		default='',
		help_text=u'Please enter the Title of tab 4',
		max_length=32,
		)
	tab4_slug = models.SlugField('Tab Slug 4',
		blank=True,
		default='',
		help_text=u'Please enter the Slug of tab 4',
		max_length=32,
		)
	tab4_text = models.TextField('Tab 4 Text',
		blank=True,
		default='',
		)
	tab5_title = models.CharField('Tab Title 5',
		blank=True,
		default='',
		help_text=u'Please enter the Title of tab 5',
		max_length=32,
		)
	tab5_slug = models.SlugField('Tab Slug 5',
		blank=True,
		default='',
		help_text=u'Please enter the Slug of tab 5',
		max_length=32,
		)
	tab5_text = models.TextField('Tab 5 Text',
		blank=True,
		default='',
		)
	tab6_title = models.CharField('Tab Title 6',
		blank=True,
		default='',
		help_text=u'Please enter the Title of tab 6',
		max_length=32,
		)
	tab6_slug = models.SlugField('Tab Slug 6',
		blank=True,
		default='',
		help_text=u'Please enter the Slug of tab 6',
		max_length=32,
		)
	tab6_text = models.TextField('Tab 6 Text',
		blank=True,
		default='',
		)
	tab7_title = models.CharField('Tab Title 7',
		blank=True,
		default='',
		help_text=u'Please enter the Title of tab 7',
		max_length=32,
		)
	tab7_slug = models.SlugField('Tab Slug 7',
		blank=True,
		default='',
		help_text=u'Please enter the slug of tab 7',
		max_length=32,
		)
	tab7_text = models.TextField('Tab 7 Text',
		blank=True,
		default='',
		)

	def __unicode__(self):
		return u'%s' % (self.tab1_title, )