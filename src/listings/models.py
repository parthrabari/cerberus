from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Table8(models.Model):
	title    		= models.CharField(max_length=56,null=True)
	platform 		= models.CharField(max_length=16,null=True)
	score   		= models.DecimalField( max_digits=2, decimal_places=1,null=True)
	genre  			= models.CharField(max_length=17,null=True)
	editors_choice 	= models.CharField(max_length=1,null=True) 
	
	def __unicode__(self):
		return self.title
    


	
	

