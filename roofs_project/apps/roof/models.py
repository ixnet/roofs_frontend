from django.db import models
from django.utils.text import slugify
from transliterate import translit
from django.core.urlresolvers import reverse
from filer.fields.image import FilerImageField

from .choices import *


class Roof(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=40)
    metro = models.CharField(max_length=30, choices=METRO_CHOICES)
    street = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField()
    building = models.CharField(max_length=5)
    porch = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    image = FilerImageField(null=True, blank=True, related_name='Крыша')
    complexity = models.CharField(max_length=10, choices=COMPLEXITY_CHOICES)
    slope = models.CharField(max_length=10, choices=SLOPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.TextField()
    route = models.TextField()

    @property
    def address(self):
        return '{0}, {1}, корпус {2}, подъезд {3}'.format(self.street, self.number, self.building, self.porch)

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, reversed=True), allow_unicode=True)
        super(Roof, self).save(*args, **kwargs)

    # View on site link from Admin
    def get_absolute_url(self):
        return reverse('roof:detail', args=[str(self.slug)])

    def __str__(self):
        return self.title
