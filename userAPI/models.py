# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Genre (models.Model):
    idGenre = models.AutoField(primary_key=True) 
    genreName = models.CharField(max_length=200)
    def __str__(self):
        return self.genreName
