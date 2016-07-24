from __future__ import unicode_literals

from django.db import models

# Create your models here.
upload = "imageProduct"


class Category(models.Model):
    ct_name = models.CharField(max_length=255)
    ct_description = models.TextField(max_length=2000, blank=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return "%s" % self.ct_name

#     def __str__(self):
#         return "%s" % self.ct_name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=4000, blank=True)
    image = models.ImageField(upload_to=upload, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return "%s" % self.name

#     def __str__(self):
#         return "%s" % self.pr_name


class ImageProduct(models.Model):
    producto = models.ForeignKey(Product)
    image = models.ImageField(upload_to=upload)
