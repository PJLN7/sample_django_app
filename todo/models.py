# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TodoItem(models.Model):
  # define TodoItem class, inherting Model

  content = models.TextField()
  # define the properties of every TodoItem