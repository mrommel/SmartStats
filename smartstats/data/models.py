from django.db import models

# Create your models here.
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

"""
	
"""
class CoordianteCountryMapping(models.Model):
	country = models.CharField(max_length=5)
	lon = models.FloatField(default=0)
	lat = models.FloatField(default=0)
	
	def __unicode__(self):			  
		return u'%.2f, %.2f=> %s' % (self.lon, self.lat, self.country)