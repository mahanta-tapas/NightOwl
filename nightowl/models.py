from django.db import models
from pygments.lexers import  get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User



class Movdata(models.Model):
    name = models.CharField(max_length=200,unique=True)
    lat = models.FloatField()
    long = models.FloatField()
    rating = models.IntegerField()
    price2 = models.IntegerField()
    owner = models.ForeignKey('auth.User',related_name='nightowl')

    def save(self, *args, **kwargs):
        super(Movdata, self).save(*args, **kwargs)

    def __unicode__(self):
        return (self.name)
