from django.db import models
from django.utils.text import slugify
from transliterate import translit

from .choices import *


class Roof(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    metro = models.CharField(max_length=30, choices=METRO_CHOICES)
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=5)
    building = models.CharField(max_length=5)
    porch = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    complexity = models.CharField(max_length=10, choices=COMPLEXITY_CHOICES)
    slope = models.CharField(max_length=10, choices=SLOPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.TextField()
    route = models.TextField()

    @property
    def address(self):
        return '{0}, {1}, корпус {2}, подъезд {3}, этаж {4}'.format(self.street, self.number, self.building, self.porch, self.floor)

    # TODO: slug improvements, if title is not unique
    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, reversed=True), allow_unicode=True)
        super(Roof, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # TODO: obtaining coordinates
    # TODO: number and building. literals or not?
