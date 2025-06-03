from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_url = models.URLField(verbose_name="Cover Image URL",null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_star_rating(self):
        full_stars = int(float(self.rating))
        return '★' * full_stars + '☆' * (5 - full_stars)