from __future__ import unicode_literals

from django.db import models

class Subscribe(models.Model):
	email_id = models.EmailField(max_length = 254, null = True, unique = True)

	def __unicode__(self):
		return self.email_id

	# def get_absolute_url(self):
	# 	return reverse('teacher-list')

