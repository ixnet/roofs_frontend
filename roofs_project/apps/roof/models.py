from django.db import models
from django.utils.text import slugify
from transliterate import translit

from .choices import *


class Roof(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    metro = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField()  # TODO: literals
    porch = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    complexity = models.IntegerField(choices=COMPLEXITY_CHOICES, default=1)
    slope = models.IntegerField(choices=SLOPE_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.TextField()
    route = models.TextField()

    @property
    def address(self):
        return '{0}, №{1}, поздъед {2}, этаж {3}'.format(self.street, self.number, self.porch, self.floor)

    # TODO: slug improvements, if title is not unique
    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, reversed=True), allow_unicode=True)
        super(Roof, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # TODO: obtaining coordinates
