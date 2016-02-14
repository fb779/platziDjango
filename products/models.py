from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    ct_name = models.CharField(max_length=255)
    ct_description = models.TextField(max_length=200, null=True)
    
    class Meta:
        ordering = ('id',)
        
    def __unicode__(self):
        return "%s" % self.ct_name
    
#     def __str__(self):
#         return "%s" % self.ct_name


class Product(models.Model):
    pr_name = models.CharField(max_length=255)
    pr_description = models.TextField(max_length=4000, null=True)
    pr_image = models.ImageField(upload_to="imageProduct", blank=True)
    pr_category = models.ForeignKey(Category)
    #pr_company = models.ForeignKey()
    
    class Meta:
        ordering = ('id',)
        
    def __unicode__(self):
        return "%s" % self.pr_name
    
#     def __str__(self):
#         return "%s" % self.pr_name
